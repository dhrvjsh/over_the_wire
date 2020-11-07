import requests

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'


url = 'http://%s.natas.labs.overthewire.org'  % username


response = requests.post(url , auth = (username, password))
print(response.text)
 