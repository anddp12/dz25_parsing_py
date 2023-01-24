from bs4 import BeautifulSoup
import requests

# https://football.ua/italy.html


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
# ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
resp = requests.get('https://football.ua/italy.html', headers=headers).text
# resp.encoding = 'utf'
soup = BeautifulSoup(resp, 'html.parser')
# print(resp)

with open('index.html', 'w', encoding='utf8') as html:
    html.write(resp)

with open('index.html', encoding='utf8') as file:
    src = file.read()

soup1 = BeautifulSoup(src, 'lxml')
table = soup1.find('table', class_='tournament-table')
table_tr = table.find('tr')
# print(table)
print(table_tr)
