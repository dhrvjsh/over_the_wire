import requests

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'


url = 'http://%s.natas.labs.overthewire.org'  % username

response = requests.get(url, cookies = {"data":"ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}, auth = (username, password))
print(response.text)
