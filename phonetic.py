import requests
from bs4 import BeautifulSoup

def read ( word ):    
    # word = input( '請輸入中文字:' )
    url = f'https://dict.revised.moe.edu.tw/search.jsp?md=1&word={word}#searchL'

    html = requests.get(url)
    bs = BeautifulSoup(html.text,'lxml')


    try:
        data = bs.find('table' , id='searchL')
        rows = data.find_all('tr')[2]

        chi = rows.find_all('td')[1].text
        ph  = rows.find('td', class_='ph').text

        return(chi+"=>"+ph)

    except:
        return('查無資料')
