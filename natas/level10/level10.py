import requests

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'


url = 'http://%s.natas.labs.overthewire.org'  % username

response = requests.get(url,  auth = (username, password))
print(response.text)