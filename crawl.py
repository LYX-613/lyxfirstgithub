import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.autohome.com.cn/siping/')
c = r.content
soup = BeautifulSoup(c,'html.parser')
# soup = BeautifulSoup(c,'html5lib')
#print(soup)
f = soup.find('ul',{'class':'filter-ret clear'})
items = f.find_all('li',{'class':'fl clear'})
for (i,item) in enumerate(items):
    title = item.find('h3').text
    # intro = item.find('div',{'class':'d2'}).text
#print(title,'\t',intro)
img = item.find('img')['src']
print(i,title,'\t',img)