# importar la biblioteca
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

