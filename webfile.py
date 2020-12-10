import urllib, requests

def download(url = "https://github.com/imvickykumar999/Tkinter-Image_Editor/raw/main/image%20editor/haarcascade_frontalface_default.xml"):

    # user = 'imvickykumar999'
    # insta_url = f'https://api.github.com/users/{user}'
    # github_url = f'https://www.instagram.com/{user}/?__a=1'

    web_file = urllib.request.urlopen(url)
    f = url.split('/')[-1]
    if '.' in f:
        ex = ''
    else:
        ex = '.txt'
    f+=ex

    file = open(f,'w')
    for line in web_file:
        decoded_line = line.decode("utf-8", 'ignore')

        # print(decoded_line)
        file.write(f'{decoded_line}')
    file.close()

    return f

# download(url)
