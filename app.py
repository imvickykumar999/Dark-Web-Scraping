
# from HostTor import VicksTor
# import VicksTor as vix
# vix.run_server('flask')

from bs4 import BeautifulSoup as bs
from flask import Flask
import requests

# link = 'https://172.217.204.100/'                  # verify=False
link = 'https://imvickykumar999.pythonanywhere.com/' # verify=True
req = requests.get(link, verify=True)

soup = bs(req.content, 'html5lib')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return req.content

if __name__ == '__main__':
    app.run(debug=False)
