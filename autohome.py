import requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import time

t1=time.time()

r = requests.get('https://car.autohome.com.cn/price/list-0-3-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html')
c = r.text
soup = BeautifulSoup(c,'html.parser')
# content = soup.find_all('div',{'class':'list-cont'})
page_div = soup.find('div',{'class':'page'})
page = page_div.find_all('a')[-2].text

cars=[]

urls = ['https://car.autohome.com.cn/price/list-0-3-0-0-0-0-0-0-0-0-0-0-0-0-0'+str(i)+'.html' for i in range(1,11)]



def crawl_page(url):
    p_r = requests.get(url)
    p_c = p_r.text
    p_soup = BeautifulSoup(p_c,'html.parser')
    p_content = p_soup.find_all('div',{'class':'list-cont'})
    pagecar=[]
# pagecars = [res.get() for res in multi_res]
# print(content[-1])
    for car in p_content:
        carDic = {}
        carDic['picturl'] = car.find('div',{'class':'list-cont-img'}).find('img')['src']
        carDic['name'] = car.find('div',{'class':'list-cont-main'}).find('a').text
# print(name)
        carDic['score'] = car.find('span',{'class':'score-number'}).text
        pagecar.append(carDic)
    return pagecar

    # urls = ['https://car.autohome.com.cn/price/list-0-3-0-0-0-0-0-0-0-0-0-0-0-0-0'+str(i)+'.html' for i in range(1,11)] 

    # price = car.find('div',{'class':'list-cont-main'})
    # pagecars.append(carDic)
    print(cars[-1])



# from pandas import DataFrame
# df = DataFrame(cars)
# df.to_csv('cars.csv')
pool = mp. Pool()
multi_res = [pool.apply_async(crawl_page,(url,)) for url in urls]
pagecars=[res.get() for res in multi_res]

for pagecar in pagecars:
    for car in pagecar:
        cars.append(car)
print(cars)
t2=time.time()
print(t2-t1)