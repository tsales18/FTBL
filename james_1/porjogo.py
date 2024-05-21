from bs4 import BeautifulSoup
import json
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
import time
import requests

flamengo = '639950ae'
coritiba = 'd680d257'
internacional = '6f7e1f03'
botafogo = 'd9fdd9d9'
athleticoPA = '2091c619'
goias = '78c617cc'
bahia = '157b7fee'
corithians = 'bf4acd28'
cruzeiro = '03ff5eeb'
vasco = '83f55dbe'
gremio = 'd5ae3703'
bragantino = 'f98930d1'
santos = '712c528f'
fortaleza = 'a9d0ab0e'
palmeiras = 'abdce579'
fluminense = '84d9701c'
americaMG = '1f68d780'
athleticoMG = '422bb734'
cuiaba = 'f0e6fb14'
sao_paulo = '5f232eb1'

equipes = ['America','Athletico-Mineiro','Athletico-Paranaense','Bahia','Botafogo','Bragantino','Corinthians','Coritiba','Cruzeiro','Cuiaba','Flamengo','Fortaleza','Goias','Gremio','Internacional','Palmeiras','Palmeiras','Santos','Sao Paulo','Vasco']

times = [equipes[3]]
for srch in times:
    with open(f'./james_1/Dados/{srch}/Geral/{srch}.html', 'r', encoding='utf-8') as file:
        conteudo = file.read()
    soup = BeautifulSoup(conteudo, 'html.parser')
    divs_com_classe = soup.find('table', class_ = 'stats_table sortable min_width now_sortable')
    a =  divs_com_classe.find_all('td', attrs={'data-stat': 'match_report'})
    c = 0
    for iv in a:
        for god in iv:
            c += 1
            b = god.get('href')
            os.system(f"start {b}")
            pyautogui.moveTo(1200, 300, duration=0.1)
            time.sleep(4)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 's')
            pyautogui.moveTo(1600, 900, duration=0.1)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')