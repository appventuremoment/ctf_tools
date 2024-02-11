import urllib.request, urllib.error, urllib.parse

link = "http://www.chiquitooenterprise.com/password"
# Missing a whole chunk of code here!
response = urllib.request.urlopen(link)
response = response.read()
test = response.decode('utf-8')
revString = test[::-1]


answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = urllib.request.urlopen(answer)
response = response.read()
print(response.decode('utf-8'))
