# `Web Scrapped`

![image](https://github.com/imvickykumar999/Web-Scraping/assets/50515418/c435df9c-fcda-4c93-8bfe-56dac5b9cb9d)

---------------

## [`Free UpGrad Study Material and Live Session Recording`](https://colab.research.google.com/drive/1rOyQ4pDIKGKBr_XE8uACBC-mzPYgM0YF?usp=sharing)

    import requests
    from bs4 import BeautifulSoup as bs
    
    link = 'https://www.upgrad.com/learn/'
    req = requests.get(link)
    soup = bs(req.content, 'html5lib')
    
    box = soup.findAll('div', attrs = {'class':'Carousel_item__UUZAx'})
    len(box)

<br>

    for i in box:
      a = i.findAll('a')
      b = i.findAll('div', attrs = {'class':'VerticalCard_content__hEtCn'})
      print('- ', b[0].text)
      print(a[0]['href'])
      print()
      print('- ', b[1].text)
      print(a[1]['href'])
      print()

----------------------

    import requests
    from bs4 import BeautifulSoup as bs
    
    link = 'https://imvickykumar999.github.io/Web-Scraping/'
    req = requests.get(link)
    soup = bs(req.content, 'html5lib')
    
    s2 = soup.findAll('td', 
            attrs = {'class':'s2'})
    
    s3 = soup.findAll('td', 
            attrs = {'class':'s3'})

<br>

    for i,j in zip(s2, s3):
      print('- ', i.text)
      print(j.a['href'])
      print()

-------------

## [`Inshorts-news-scraping`](https://github.com/imvickykumar999/Inshorts-news-scraping/blob/main/inshorts%20news.ipynb)

    THIS REPOSITORY contains different types of useful files like, 
    web file downloader, insta post downloader, eye alignment etc.

---------------------------------

## [`https://haveibeenpwned.com/PwnedWebsites`](https://haveibeenpwned.com/PwnedWebsites)

[![image](https://user-images.githubusercontent.com/50515418/225050010-05f44b21-c1d1-462f-b848-0fb04edae760.png)](https://haveibeenpwned.com/PwnedWebsites#DominosIndia)

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

------------

-  Supply Chain ManagementA supply chain is a mechanism through which raw materials from the suppliers are first converted and then placed in the hands of the customers in the form of finished goods.
https://www.upgrad.com/learn/supply-chain-management/what-is-supply-chain-5274-31522-187492-576396-2949699/


        More Upgrad Videos
    
<details>
    
-  Organisational Behaviour and Human ResourcesLearn Organisational Behaviour and Human Resources concepts at upGrad learn platform.
https://www.upgrad.com/learn/organisational-behaviour-and-human-resources/introduction-to-strategy-5414-32461-192522-592678-3027654/

-  Product ManagementProduct Management mainly deals with the overall supervision of a product.
https://www.upgrad.com/learn/product-managment-tutorial/responsbilites-of-a-product-manager-5275-31523-187495-576402-2949714/

-  BlockchainThis module will set the foundation of all Blockchain concepts that you will learn going forward.
https://www.upgrad.com/learn/blockchain/introduction-to-blockchain-technology-5416-32467-192536-592703-3027711/

-  Object Oriented ProgrammingGet introduced to the Object-Oriented Paradigm of software development
https://www.upgrad.com/learn/object-oriented-programming-tutorial/what-is-module-in-ooad-an-overview-5405-32425-192323-592193-3025965/

-  Content MarketingLearn about content marketing and why it is important for businesses.
https://www.upgrad.com/learn/content-marketing/introduction-to-content-marketing-5418-32473-192557-592745-3027825/

-  Data Analytics In this segment you will understand how to read a typical data file and the structure of the Excel interface
https://www.upgrad.com/learn/data-analytics/understanding-the-excel-interface-5406-32430-192355-592269-3026321/

-  Problem SolvingWelcome to the  module on Problem-Solving. Understand the importance of problem-solving.
https://www.upgrad.com/learn/problem-solving/introduction-to-problem-solving-5420-32483-192586-592808-3027972/

-  JavaScriptLearn about the basics of JavaScript language in this module & understanding how to program in this language in general.
https://www.upgrad.com/learn/javascript/what-is-variables-and-datatypes-in-javascript-5407-32437-192394-592369-3026695/

-  EconomicsLearn micro & macro economics concepts at upGrad learn platform.
https://www.upgrad.com/learn/economics/how-much-do-my-consumers-want-understanding-consumers-need-5422-324870-192600-592837-3028030/

-  Data ScienceLearn data science concepts from the basic and upskill yourself.
https://www.upgrad.com/learn/data-science/the-foundation-of-linear-algebra-vectors-5409-32583-193001-593870-3032391/

-  HealthcareLearn healthcare concepts at upGrad learn platform
https://www.upgrad.com/learn/healthcare/eskills-in-healthcare-overview-5423-32497-192633-592902-3028183/

-  Marketing FundamentalsLearn marketing fundamentals concepts from the basic and upskill yourself.
https://www.upgrad.com/learn/marketing-fundamentals/course-overview-marketing-fundamentals-5399-32534-192745-593167-3029038/

-  Professional ImprovementLearn all the professional improvement concepts at upGrad learn platform.
https://www.upgrad.com/learn/professional-improvement/what-is-stress-5425-32499-192639-592917-3028216/

-  RegressionLearn regression concepts from the scratch and get expertise in statistical techniques.
https://www.upgrad.com/learn/regression/introduction-to-simple-linear-regression-in-python-5400-32514-192679-593010-3028524/

-  Emerging TechLearn all the emerging tech concepts at upGrad learn platform
https://www.upgrad.com/learn/emerging-tech/basics-of-cloud-computing-5427-32511-192672-592989-3028466/

-  PythonWelcome to the course on Python for Data Science. In this course, you will learn to write basic Python programs required for working with data.
https://www.upgrad.com/learn/python/introduction-to-basics-of-python-5398-32506-192657-592955-3028352/

-  AccountingLearn all the accounting related concepts at upGrad learn platform
https://www.upgrad.com/learn/accounting/learning-note-accounting-fundamentals-5411-32446-192429-592448-3027043/

-  Effective CommunicationLearn effective communication skills at upGrad learn platform and have a successful career.
https://www.upgrad.com/learn/effective-communication/how-to-feel-comfortable-while-conversing-with-others-5397-32475-192566-592766-3027877/

-  JournalismLearn all the journalism related concepts at upGrad learn platform
https://www.upgrad.com/learn/journalism/development-journalism-brief-history-and-meaning-5415-32466-192533-592697-3027702/

-  Social Media and Email MarketingLearn about some best practices to be followed while posting organic content on social platforms.
https://www.upgrad.com/learn/social-media-and-email-marketing/linkedin-organic-content-best-practices-5413-32458-192506-592641-3027542/

-  LawLearn all the law related concepts at upGrad platform
https://www.upgrad.com/learn/law/why-soft-skills-matters-for-lawyers-5417-32479-192574-592783-3027900/

-  Developing Logic in Programming
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/190484/MU7CJTINhnselJfYn76fBgM6uoyBo1Xg.mp4

-  Developing Logic in Programming
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/190528/aDc6eNk7wJIEhnyB4V1LGoWdSSA0i2E7.mp4

-  Hands-on Python Syntaxes
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/190486/mXIZXnPcJ3KsaAATcLspjEUsMdiWq189.mp4

-  Hands-on Python Syntaxes
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/190487/rY4pofHwX5XZHJudvHb4wYZSPGesutVz.mp4

-  Introduction to Python Data Structures - Slot 2
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/191474/gSrdsu4FxqdEgoWVTLaOtk82cpz591GV.mp4

-  Introduction to Python Data Structures - Slot 1
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/191476/HoMZFyzUPgMQ1q42DSBj9UGB3N5yUYCg.mp4

-  Hands-on Python Data Structures - Slot 2
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/191477/yshkhwezaxFl8oxqu02Xo338b9ijevxD.mp4

-  Hands-on Python Data Structures - Slot 1
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/191475/EfNYfkht1vnthZMKvyY21pXqaMTh1drK.mp4

-  Instructor-Led Coding Practice
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/192512/UYdAlQhS1H9IILW2uqoVYzH3pq9x7Xdh.mp4

-  Instructor-Led Coding Practice
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/192511/kDwoGgJUyyiZC1fTNhXJxYTgGSR4ecCM.mp4

-  Hands-on Numpy
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/193393/dX0AUcuGQMFg19rfPmZ6gnNBKhvMAfrX.mp4

-  Hands-on Numpy
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/193394/Rj8PFWW0mAJwyCyGpWoBYoD0CIJQWGaa.mp4

-  Hands-on Pandas
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/193396/TdJ3qF3kJAk9nzIOmjlrV4a7eQE12KQp.mp4

-  Hands-on Pandas
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/193395/D7RGyQKaTgeGci8OwXXKyYP5Oa1TokeR.mp4

-  Data Visualisation Theory Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/168524/5GXWNeKDOgxg7BWp4M2z8PtFOj0ryyl9.mp4

-  Instructor-Led Live Coding Session on EDA
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/169975/QrFsCudTP5G9aQE2VTfd0otCuJo6yHn9.mp4

-  EDA: Methodologies and Best Practices
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/170560/Te8mAOjxcCPehi75VsEWE3DaSsppxsGG.mp4

-  EDA Career Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/170564/GMLStFa4W9OJDRaKKTRG6Wr925j1oKqi.mp4

-  Credit EDA pre assignment session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/171965/gLArs1Szw12GjVuH8Kr9gs4LAm2DxIXn.mp4

-  Theoretical Session on Inferential Statistics
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/173111/cl9qkCNpmrCHiFhP5RV869acqbX55y6S.mp4

-  Whiteboard session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/175217/CdwMUD3vfbz9dMaNFdABgA6ns3EE7bb1.mp4

-  Live Coding Session - SQL - A
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/176330/6Ujz7mQ3hMAKrCQ6o2xiigYJY19mxPec.mp4

-  Live Coding Session - SQL - B
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/176331/K5A4q5wyNDv2WZSNEgxvqEHUC92IjJ8L.mp4

-  Statistics Career Session - A
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/176334/QOOw4RQdHFLrt1B8f10XDCTHf1lS6oWK.mp4

-  Statistics Career Session - B
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/176336/jQJoupNYTKDrCGAwwOETSWPA2851xIBM.mp4

-  SQL Career Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/177546/oQ978LZZpT3AnellV9JNZGBTxoHXux5V.mp4

-  SQL Career Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/177547/zXsoDHkGpoUZcjj9InI7Hmdpsc9q4Zi7.mp4

-  Doubt Solving Session with Prof RC
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/177548/2NvmQaaulcQc0Odbj8O1Aefwc5NV4NJp.mp4

-  SQL Case Study Pre-Assignment Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/179177/ZEzu2YLMYnq8Mv3alZuo3dJEf0aPgqg5.mp4

-  SQL Case Study Pre-Assignment Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/179178/49XI2hsBHqo9sJf0NU3I3hhJ0nUd5ZUZ.mp4

-  Course 1 Revision Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/179179/JLDJiBx3Kewnixjl6b0LkWjhuwP0pI84.mp4

-  Course 1 Revision Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/179180/xdVSd6j0JCaItdnQIwG8f6X695n7pRVg.mp4

-  Doubt Solving Session with Prof. RC
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/179549/KLyAhceQz0PGtKnT7NRNjOPvKtgLJblz.mp4

-  Linear Regression Conceptual Session - Slot 1
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/181608/xZOGX2sYWZAV1NczatovZ6PBO87hFC2e.mp4

-  Linear Regression Conceptual Session - Slot 2
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/181609/e2YoD2rrOKXFDNWnpiXgnjTejsOI5cJk.mp4

-  Linear Regression Pre-Assignment Live Session - Slot 1
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/184066/PaCVg9Acj6GNpCArbT7kBVFmthBZiT0v.mp4

-  Linear Regression Pre-Assignment Live Session - Slot 2
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/184783/P149jhQRbDjidESsFdUVnWsCtiDG0O40.mp4

-  Adhoc Session - Linear Regression
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/184068/g2cNsGNApJlWmw78SaehwCkf3gcrW7it.mp4

-  Whiteboard week
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/186803/DvztyiNKYz338prE4WnBWKu4kQlEDREv.mp4

-  Working with Tree Models Slot 1
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/188053/V9C6NWJPELw27MXuREt0QSqijqkbQVpD.mp4

-  Working with Tree Models Slot 2
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/188054/txx6Cqjp6NeGxrVR5ycQ6WJAvC50NXzI.mp4

-  Clustering Live Coding Session Slot 1
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/189820/EilTquPVzBLw1pxG47bEIwTMmMEDGhNy.mp4

-  Clustering Live Coding Session Slot 2
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/189381/VFxA7JL364VgrqAE9TZY9p0tStB4UnUN.mp4

-  Working with Text Data
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/190478/VJvYIsECOa3h4MYVUAIHvVsuQdAGCdZe.mp4

-  Working with Text Data
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/190479/A36D04IpoUly0Xt3lPbNngYpja00YttZ.mp4

-  ML Session with Hiring Manager
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/191456/Wgx5ZxCF1neCghaqeOaGZNOcWhwj5Ozw.mp4

-  ML Session with Hiring Manager
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/191457/kT7PCMnP9neYCbsKAmKbZXRa99GMZzt4.mp4

-  Lead Scoring Case Study Pre-Assignment Live Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/192496/cs3m5DOjZKFwYTrDnejinBEpqh5R8Ys4.mp4

-  Lead Scoring Case Study Pre-Assignment Live Session
https://live-session-recording-service.s3.ap-south-1.amazonaws.com/production/192828/j9wRXrfl6xr4lyn2bazZSrO69aqSxOfb.mp4

</details>
