import urllib.request
from IPython.display import Image, display
import requests

def insta(username = 'imvickykumar999'):
    link = f'https://www.instagram.com/{username}/?__a=1'
    response = requests.get(link).json()
    graph = response['graphql']['user']

    value = [
        graph['username'],
        graph['full_name'],
        graph['edge_followed_by']['count'],
        graph['edge_follow']['count'],
        graph['biography'],
        graph['is_private'],
        graph['profile_pic_url_hd'], ]

    key = ['username', 'full_name', 'followers', 'following',
           'biography', 'is_private', 'profile_pic_url_hd', ]

    insta = dict(zip(key, value))
    return insta, response, link

# username = input('Enter username : ')

def dp(username = 'imvickykumar999'):
    dinsta = insta(username)[0]
    image_url = dinsta['profile_pic_url_hd'] #the image on the web
    save_name = f'{username}.jpg' #local name to be saved
    urllib.request.urlretrieve(image_url, save_name)

# display(Image(url = dinsta['profile_pic_url_hd']))
# print(dinsta)
