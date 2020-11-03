import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'


url = 'http://%s.natas.labs.overthewire.org'  % username

response = requests.post(url + '/includes/secret.inc', auth = (username, password))
print(response.text)