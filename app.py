
# from HostTor import VicksTor
import VicksTor as vix
vix.run_server('flask')

from bs4 import BeautifulSoup as bs
from flask import Flask
import requests

link = 'https://haveibeenpwned.com/PwnedWebsites'
req = requests.get(link)

soup = bs(req.content, 'html5lib')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return req.content

if __name__ == '__main__':
    app.run(debug=False)
