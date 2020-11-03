import requests
import base64
import urllib

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'


url = 'http://%s.natas.labs.overthewire.org'  % username

response = requests.get(url, auth = (username, password))
print(base64.b64decode(urllib.parse.unquote(response.cookies['data'])).hex())
