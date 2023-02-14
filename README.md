# [Inshorts-news-scraping](https://github.com/imvickykumar999/Inshorts-news-scraping/blob/main/inshorts%20news.ipynb)

THIS REPOSITORY contains different types of useful files like, web file downloader, insta post downloader, eye alignment etc.

---------------------------------

    import requests
    from bs4 import BeautifulSoup as bs

    link = 'https://inshorts.com/en/read'
    req = requests.get(link)

    soup = bs(req.content, 'html5lib')
    box = soup.findAll('div', attrs = {'class':'news-card z-depth-1'})

----------------------

# https://www.scrapethissite.com/pages/simple/

![image](https://user-images.githubusercontent.com/50515418/218786512-4b639301-4cec-4053-917f-075b630d98ee.png)
