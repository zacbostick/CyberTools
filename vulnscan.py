import requests

target_url = 'https://example.com'
common_vulnerabilities = [
    'admin.php',
    'login.php',
    'test.php',
    'robots.txt'
]

for vulnerability in common_vulnerabilities:
    url = f'{target_url}/{vulnerability}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Vulnerability found: {url}')
