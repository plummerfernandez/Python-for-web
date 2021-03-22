
import requests
from bs4 import BeautifulSoup
import shutil

websiteMain = "https://www.plummerfernandez.com"
result = requests.get(websiteMain)
print(result.status_code)
src = result.content

soup = BeautifulSoup(src, 'html.parser')

#print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
#print(soup.find_all('a'))

# print("Listing all links on page:")
# for link in soup.find_all('a'):
# 	print(link.get('href'))

#print(soup.get_text())

print("Listing all images on page:")
for images in soup.find_all('img'):
	try:
		image_url = print(websiteMain + str(images.get('src')))
		r = requests.get(image_url, stream = True)
		with open(filename,'wb') as f:
			shutil.copyfileobj(r.raw, f)
	except:
		print("whoops!!")

#adapted from 
#https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c