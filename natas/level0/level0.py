import requests
import re


userrname = 'natas0'
password = 'natas0'

url = 'http://%s.natas.labs.overthewire.org/'  % userrname

response = requests.get(url,  auth = (userrname, password))

print(response.text)
