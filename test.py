import requests
from bs4 import BeautifulSoup

# word = input('請輸入一個字')
def chinese(word):
    url = f'https://www.twpen.com/{word}.html'

    html = requests.get(url)
    bs = BeautifulSoup(html.text,'lxml')

    try:
        dat = bs.find_all('div', class_='site-article-hanziinfo')
        rad = (dat[0].find_all('p'))[0].text[:-1]
        num = (dat[0].find_all('p'))[1].text[:-1]
        chi = (dat[0].find_all('p'))[2].text
        eng = (dat[0].find_all('p'))[3].text

        
        dic = {rad,num}
        return(dic)

    except:
        return('查無資料,請輸入一個字的國字')
