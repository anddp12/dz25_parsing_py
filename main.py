from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv

# https://football.ua/italy.html
cur_date = datetime.now().strftime('%Y_%m_%d')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
# ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
resp = requests.get('https://football.ua/italy/table.html', headers=headers).text
# resp.encoding = 'utf'
soup = BeautifulSoup(resp, 'html.parser')
# print(resp)

with open('index.html', 'w', encoding='utf8') as html:
    html.write(resp)

with open('index.html', encoding='utf8') as file:
    src = file.read()

soup1 = BeautifulSoup(src, 'lxml')
table = soup1.find('table', class_='main-tournament-table')
date_th = table.find('tr').find_all('th')
# print(date_th)

table_th = []
for tr in date_th:
    tr = tr.text.strip()
    table_th.append(tr)
# print(table_th)

with open(f'date{cur_date}.csv','w',encoding='utf8')as file:
    writen = csv.writer(file)
    writen.writerow(
        (
            table_th
        )
    )

tbody_tr = table.find_all('tr')
# print(tbody_tr)

for td in tbody_tr:
    num = table.find('td', class_="num").text
    team = table.find('td', class_="team").find('a').text
    games = table.find('td', class_="games").text
    win = table.find('td', class_="win").text
    draw = table.find('td', class_="draw").text
    lose = table.find('td', class_="draw").text
    goal = table.find('td', class_="goal").text
    miss = table.find('td', class_="miss").text
    diff = table.find('td', class_="diff").text
    score = table.find('td', class_="score").text
    form = table.find('td', class_="form").text
    
# print(num, team, games, win, draw,lose,goal, miss, diff, score, form)

with open(f'date{cur_date}.csv','a',encoding='utf8')as file:
    writen = csv.writer(file)

    writen.writerow(
        (
            num, team, games, win, draw, lose, goal, miss, diff, score, form
        )
    )
