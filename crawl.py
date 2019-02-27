from bs4 import BeautifulSoup
import urllib.request
import csv
import pandas as pd
url = 'https://www.google.com/shopping/product/13635365085400395108/reviews?q=t3+hair+dryer&biw=1440&bih=790&prds=paur:ClkAsKraX6We39utj0ixB2R8C71i_vDC0FouhZlPYYW3TvlagoXRrB6r1JEBVHntUJYH6o72H0kGhHuPpN2b-aG3aRnpzlWlkfHaMf-Qiw2M_uKF888Q73yO2RIZAFPVH72Iom_AMhBfPADnzsRFzTogSLEF0w&sa=X&ved=0ahUKEwjBx6eLj_3eAhWGmuAKHVfwCQgQqSQIuQE'
ourUrl=urllib.request.urlopen(url)
soup=BeautifulSoup(ourUrl,'html.parser')
data ={}
content_list = []
rating_list=[]
date_list=[]
source_list=[]
title_list=[]
id_list=[]
out = open('t3hair.csv', 'a')
outcsv = csv.writer(out)
outcsv.writerow(["id","rating","date","source","title","content"])


for i in soup.find_all('div',{'class':'review-content'}):
    content=i.find('span')
    new_content=str(content).replace('<br/>','').replace('<span>','').replace('</span>','')
    content_list.append(new_content)
data['content']=content_list
for i in soup.find_all('div',{'class':'review-rating'}):
    rating= i.find('div').get('aria-label')
    rating = str(rating).split()
    rating_list.append(rating[0])
data['rating']=rating_list
    #print(new_content,out='rawdata.csv',end='\t')
for i in soup.find_all('div',{'class':'review-rating'}):
    date = i.contents[2].strip().split('-')
    date = date[1].strip()
    date_list.append(date)
data['date']=date_list
for i in soup.find_all('div',{'class':'review-rating'}):
    source=i.contents[3].get_text()
    source_list.append(source)
data['source']=source_list
for i in soup.find_all('div',{'class':'review-title'}):
    title=i.get_text()
    title_list.append(title)
data['title']=title_list
for i in soup.find_all('div',{'class':'review-rating'}):
    id = i.contents[2].strip().split('-')
    id = id[0].split()
    id = id[1]
    id_list.append(id)
data['id']=id_list
out = open('t3hair.csv', 'a')
outcsv = csv.writer(out)

n = 0
while n< 10:
    outcsv.writerow([str(data['id'][n]),str(data['rating'][n]),str(data['date'][n]),str(data['source'][n]),str(data['title'][n]),str(data['content'][n])])
    n+=1
    l = 10
    while l < 440:
        data ={}
        content_list = []
        rating_list=[]
        date_list=[]
        source_list=[]
        title_list=[]
        id_list=[]
        url = 'https://www.google.com/shopping/product/13635365085400395108/reviews?q=t3%20hair%20dryer&biw=1440&bih=790&prds=paur:ClkAsKraX6We39utj0ixB2R8C71i_vDC0FouhZlPYYW3TvlagoXRrB6r1JEBVHntUJYH6o72H0kGhHuPpN2b-aG3aRnpzlWlkfHaMf-Qiw2M_uKF888Q73yO2RIZAFPVH72Iom_AMhBfPADnzsRFzTogSLEF0w,rstart:'+str(l)
        ourUrl=urllib.request.urlopen(url)
        soup=BeautifulSoup(ourUrl,'html.parser')

        for i in soup.find_all('div',{'class':'review-content'}):
            content=i.find('span')
            new_content=str(content).replace('<br/>','').replace('<span>','').replace('</span>','')
            content_list.append(new_content)
        data['content']=content_list
        for i in soup.find_all('div',{'class':'review-rating'}):
            rating= i.find('div').get('aria-label')
            rating = str(rating).split()
            rating_list.append(rating[0])
        data['rating']=rating_list
            #print(new_content,out='rawdata.csv',end='\t')
        for i in soup.find_all('div',{'class':'review-rating'}):
            date = i.contents[2].strip().split('-')
            date = date[1].strip()
            date_list.append(date)
        data['date']=date_list
        for i in soup.find_all('div',{'class':'review-rating'}):
            source=i.contents[3].get_text()
            source_list.append(source)
        data['source']=source_list
        for i in soup.find_all('div',{'class':'review-title'}):
            title=i.get_text()
            title_list.append(title)
        data['title']=title_list
        for i in soup.find_all('div',{'class':'review-rating'}):
            id = i.contents[2].strip().split('-')
            id = id[0].split()
            try:
                id=id[1]
                id_list.append(id)
            except:
                id_list.append('')
        data['id']=id_list

        n = 0

        while n< 10:
            outcsv.writerow([str(data['id'][n]),str(data['rating'][n]),str(data['date'][n]),str(data['source'][n]),str(data['title'][n]),str(data['content'][n])])
            n+=1

        l += 10
        data.clear()


    out.close()
