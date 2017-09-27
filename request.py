import requests

r = requests.get('https://babe.kde.org')
print(r.text)
