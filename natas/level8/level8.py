import requests

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'


url = 'http://%s.natas.labs.overthewire.org'  % username

response = requests.get(url, auth = (username, password))
print(response.text)