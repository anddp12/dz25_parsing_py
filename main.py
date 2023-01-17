import bs4
import requests, sys, os

import bs4
import requests, sys, os


# Потрібен парсер оголошень ОЛХ по рубрикам який буде вигружати в Excel таблицю такі дані: заголовок, опис, кількість переглядів
# https://freelancehunt.com/project/parser-ogoloshen-olh/1160960.html

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
resp = requests.get('https://www.olx.ua/d/uk/dom-i-sad/instrumenty/generatory/?utm_source=olx&utm_medium=virtual_category&utm_campaign=generator_for_blackout', headers=headers)
resp.encoding = 'utf'
print(os.cpu_count())

if resp.status_code == 200:
    resp = resp.text
    # print(resp)
else:
    sys.exit()
    os.cpu_count()

soup = bs4.BeautifulSoup(resp, 'html.parser')

title1 =  soup.find('h6', class_='css-16v5mdi er34gjf0').getText()
price1 =  soup.find('span', class_='css-1c0ed4l').getText()

print(title1, price1)