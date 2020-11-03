import requests

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'


url = 'http://%s.natas.labs.overthewire.org'  % username

response = requests.get(url, auth = (username, password))
print(response.text)