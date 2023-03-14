# [`Inshorts-news-scraping`](https://github.com/imvickykumar999/Inshorts-news-scraping/blob/main/inshorts%20news.ipynb)

    THIS REPOSITORY contains different types of useful files like, 
    web file downloader, insta post downloader, eye alignment etc.

---------------------------------

## [`https://haveibeenpwned.com/PwnedWebsites`](https://haveibeenpwned.com/PwnedWebsites)

> [![image](https://user-images.githubusercontent.com/50515418/225050010-05f44b21-c1d1-462f-b848-0fb04edae760.png)](https://haveibeenpwned.com/PwnedWebsites#DominosIndia)

----------------------------

    import requests
    from bs4 import BeautifulSoup as bs

    link = 'https://haveibeenpwned.com/PwnedWebsites'
    req = requests.get(link)

    soup = bs(req.content, 'html5lib')
    box = soup.findAll('div', attrs = {'class':'news-card z-depth-1'})
    
    # len(box) == 667
    print(link + box[0].findAll('p')[1].a['href']) 
    
----------------------

## [`https://www.scrapethissite.com/pages/simple`](https://www.scrapethissite.com/pages/simple)

![image](https://user-images.githubusercontent.com/50515418/218786512-4b639301-4cec-4053-917f-075b630d98ee.png)
