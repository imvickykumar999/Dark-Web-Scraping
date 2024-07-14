from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import os

requests = RequestsTor(tor_ports=(9050,), tor_cport=9051)
# url = 'http://7ravv2cin5iyoyszsg6sobpp4jsgtyp5r5tpacmuyvadjjyhdwjzgxyd.onion/' # crud website
url = 'http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/' # news website

def fetch_and_save(url, session, folder='resources'):
    response = session.get(url)
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, os.path.basename(url))
    with open(file_path, 'wb') as f:
        f.write(response.content)
    return file_path

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Process and save CSS files
        for link in soup.find_all('link', rel='stylesheet'):
            css_url = link.get('href')
            if css_url.startswith('http'):
                css_file = fetch_and_save(css_url, requests)
                link['href'] = css_file
            elif css_url.startswith('/'):
                css_file = fetch_and_save(url + css_url, requests)
                link['href'] = css_file

        # Process and save JS files
        for script in soup.find_all('script', src=True):
            js_url = script.get('src')
            if js_url.startswith('http'):
                js_file = fetch_and_save(js_url, requests)
                script['src'] = js_file
            elif js_url.startswith('/'):
                js_file = fetch_and_save(url + js_url, requests)
                script['src'] = js_file

        # Save the modified HTML
        with open('output.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))

        print("Page and resources saved successfully.")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

fetch_page(url)
