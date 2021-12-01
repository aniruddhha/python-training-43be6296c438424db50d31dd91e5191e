import requests

re = requests.get('https://google.com')
print(f'{re.text}')
