# [`Free UpGrad Study Material`](https://colab.research.google.com/drive/1rOyQ4pDIKGKBr_XE8uACBC-mzPYgM0YF?usp=sharing)

    import requests
    from bs4 import BeautifulSoup as bs
    
    link = 'https://www.upgrad.com/learn/'
    req = requests.get(link)
    soup = bs(req.content, 'html5lib')
    
    box = soup.findAll('div', 
            attrs = {'class':'Carousel_item__UUZAx'})
    
    len(box)
    # 11

<br>

    for i in box:
      a = i.findAll('a')
      print('- ', a[0]['href'])
      print('- ', a[1]['href'])


-  https://www.upgrad.com/learn/supply-chain-management/what-is-supply-chain-5274-31522-187492-576396-2949699/
-  https://www.upgrad.com/learn/organisational-behaviour-and-human-resources/introduction-to-strategy-5414-32461-192522-592678-3027654/
-  https://www.upgrad.com/learn/product-managment-tutorial/responsbilites-of-a-product-manager-5275-31523-187495-576402-2949714/
-  https://www.upgrad.com/learn/blockchain/introduction-to-blockchain-technology-5416-32467-192536-592703-3027711/
-  https://www.upgrad.com/learn/object-oriented-programming-tutorial/what-is-module-in-ooad-an-overview-5405-32425-192323-592193-3025965/
-  https://www.upgrad.com/learn/content-marketing/introduction-to-content-marketing-5418-32473-192557-592745-3027825/
-  https://www.upgrad.com/learn/data-analytics/understanding-the-excel-interface-5406-32430-192355-592269-3026321/
-  https://www.upgrad.com/learn/problem-solving/introduction-to-problem-solving-5420-32483-192586-592808-3027972/
-  https://www.upgrad.com/learn/javascript/what-is-variables-and-datatypes-in-javascript-5407-32437-192394-592369-3026695/
-  https://www.upgrad.com/learn/economics/how-much-do-my-consumers-want-understanding-consumers-need-5422-324870-192600-592837-3028030/
-  https://www.upgrad.com/learn/data-science/the-foundation-of-linear-algebra-vectors-5409-32583-193001-593870-3032391/
-  https://www.upgrad.com/learn/healthcare/eskills-in-healthcare-overview-5423-32497-192633-592902-3028183/
-  https://www.upgrad.com/learn/marketing-fundamentals/course-overview-marketing-fundamentals-5399-32534-192745-593167-3029038/
-  https://www.upgrad.com/learn/professional-improvement/what-is-stress-5425-32499-192639-592917-3028216/
-  https://www.upgrad.com/learn/regression/introduction-to-simple-linear-regression-in-python-5400-32514-192679-593010-3028524/
-  https://www.upgrad.com/learn/emerging-tech/basics-of-cloud-computing-5427-32511-192672-592989-3028466/
-  https://www.upgrad.com/learn/python/introduction-to-basics-of-python-5398-32506-192657-592955-3028352/
-  https://www.upgrad.com/learn/accounting/learning-note-accounting-fundamentals-5411-32446-192429-592448-3027043/
-  https://www.upgrad.com/learn/effective-communication/how-to-feel-comfortable-while-conversing-with-others-5397-32475-192566-592766-3027877/
-  https://www.upgrad.com/learn/journalism/development-journalism-brief-history-and-meaning-5415-32466-192533-592697-3027702/
-  https://www.upgrad.com/learn/social-media-and-email-marketing/linkedin-organic-content-best-practices-5413-32458-192506-592641-3027542/
-  https://www.upgrad.com/learn/law/why-soft-skills-matters-for-lawyers-5417-32479-192574-592783-3027900/

 ------------

## [`Inshorts-news-scraping`](https://github.com/imvickykumar999/Inshorts-news-scraping/blob/main/inshorts%20news.ipynb)

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
