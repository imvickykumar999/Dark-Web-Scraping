import requests
from bs4 import BeautifulSoup as bs

link = 'https://haveibeenpwned.com/PwnedWebsites'
req = requests.get(link)

soup = bs(req.content, 'html5lib')
print(soup)
