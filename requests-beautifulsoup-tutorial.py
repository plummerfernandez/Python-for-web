
import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.google.co.uk")
print(result.status_code)
src = result.content

soup = BeautifulSoup(src, 'html.parser')

print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
#print(soup.find_all('a'))

print("Listing all links on page:")
for link in soup.find_all('a'):
	print(link.get('href'))
