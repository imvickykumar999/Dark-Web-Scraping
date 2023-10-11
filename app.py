
# # from HostTor import VicksTor
# import VicksTor as vix
# vix.run_server('flask')

from bs4 import BeautifulSoup as bs
from flask import Flask
import requests, socket

import pandas as pd
df = pd.read_csv('ip address/IpAddress.csv')
print(df)

def getIP(site):
    try:
        site = socket.gethostbyname(site)
    except:
        site = socket.gethostbyname(site.split('/')[2])

    slash = f'https://{site}/'
    print(slash, end='\n\n')
    return slash, False

site = input('\nEnter link : ')
if site == '':
    site = 'https://github.com/imvickykumar999'
    # site = 'https://socheers.net/'

link = getIP(site) # link by IP Address
# link = site, True # link with SSL verified

req = requests.get(link[0], verify=link[1])
soup = bs(req.content, 'html5lib')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return req.content

if __name__ == '__main__':
    app.run(debug=False)
