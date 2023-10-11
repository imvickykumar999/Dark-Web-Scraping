from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import socket

def getIP(site):
  try:
    site = socket.gethostbyname(site)
  except:
    site = socket.gethostbyname(site.split('/')[2])
  return f'https://{site}/'

soup = bs(open('mytable.html'), 'html.parser')
lst = soup.find_all('span', class_='tw-table__row-domain')

domain=[]
ipadd=[]

for i in lst:
  try:
    ipadd.append(getIP(i.text))
    domain.append(i.text)
  except:
    pass

df = pd.DataFrame(list(zip(domain, ipadd)))
df.columns =['Domain Name', 'IP Address']

df.index +=1
df.index.name = 'S.No.'
df.to_csv('IpAddress.csv')

# ---------------------

link = 'https://172.217.204.100/'
req = requests.get(link, verify=False)

soup = bs(req.content, 'html5lib')
# print(soup)
