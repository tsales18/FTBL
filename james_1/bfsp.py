from bs4 import BeautifulSoup
import json
import pandas as pd

# Carregar o conteúdo do arquivo HTML
with open('./james_1/Dados/Flamengo/Geral/geral_FL.html', 'r', encoding='utf-8') as file:
    conteudo = file.read()
# Criar um objeto BeautifulSoup
soup = BeautifulSoup(conteudo, 'html.parser')
# Exemplo: Encontrar todos os links (elementos <a>)

divs_com_classe = soup.find('table', class_ = 'stats_table sortable min_width now_sortable sticky_table eq1 re1 le1')

lista_player = []
lista_nationality = []
lista_position = []
lista_age = []
lista_games = []
lista_games_starts = []
lista_minutes = []
lista_minutes_90s = []
lista_goals = []
lista_assists = []
lista_assists_per90 = []
lista_goals_assists = []
lista_goals_pens = []
lista_pens_made = []
lista_pens_att = []
lista_cards_yellow = []
lista_cards_red = []
lista_xg = []
lista_npxg = []
lista_xg_assist = []
lista_npxg_xg_assist = []
lista_progressive_carries = []
lista_progressive_passes = []
lista_progressive_passes_received = []
lista_goals_per90 = []
lista_goals_assists_per90 = []
lista_goals_pens_per90 = []
lista_goals_assists_pens_per90 = []
lista_xg_per90 = []
lista_xg_assist_per90 = []
lista_npxg_per90 = []
lista_xg_xg_assist_per90 = []
lista_matches = []
lista_npxg_xg_assist_per90 = []

listas = [[lista_nationality],[lista_position],[lista_age],[lista_games],[lista_games_starts],[lista_minutes],[lista_minutes_90s],
          [lista_goals],[lista_assists],[lista_goals_assists],[lista_goals_pens],[lista_pens_made],[lista_pens_att],[lista_cards_yellow],[lista_cards_red],
          [lista_xg],[lista_npxg],[lista_xg_assist],[lista_npxg_xg_assist],[lista_progressive_carries],[lista_progressive_passes],
          [lista_progressive_passes_received],[lista_goals_per90],[lista_assists_per90],[lista_goals_assists_per90],[lista_goals_pens_per90],[lista_goals_assists_pens_per90],[lista_xg_per90],
          [lista_xg_assist_per90],[lista_npxg_per90],[lista_xg_xg_assist_per90],[lista_npxg_xg_assist_per90],[lista_matches]]

tipo_1 = ['nationality','position','age','games','games_starts','minutes','minutes_90s','goals','assists','goals_assists','goals_pens',
         'pens_made','pens_att','cards_yellow','cards_red','xg','npxg','xg_assist','npxg_xg_assist','progressive_carries','progressive_passes',
         'progressive_passes_received','goals_per90','assists_per90','goals_assists_per90','goals_pens_per90','goals_assists_pens_per90','xg_per90',
         'xg_assist_per90','xg_xg_assist_per90','npxg_per90','npxg_xg_assist_per90','matches']

a =  divs_com_classe.find_all('th', attrs={'data-stat': 'player'})
for iv in a:
    v = iv.text
    lista_player.append(v)
c = 0
for srch in tipo_1:
    c += 1
    a =  divs_com_classe.find_all('td', attrs={'data-stat': f'{srch}'})
    for iv in a:
        v = iv.text
        listas[c-1][0].append(v)
    dados = {
    'Jogador' : f'{lista_player}',
    'Nação' : f'{listas[0][0]}',
    'Posição' : f'{listas[1][0]}',
    'Idade' : f'{listas[2][0]}',
    'Jogos Disputados' : f'{listas[3][0]}',
    'Jg. inciados' : f'{listas[4][0]}',
    'Minutos Jgds.' : f'{listas[5][0]}',
    '90s jgds.' : f'{listas[6][0]}',
    'Gols' : f'{listas[7][0]}',
    'Assis' : f'{listas[8][0]}',
    'Gols e Assis' : f'{listas[9][0]}',
    'Gols normais' : f'{listas[10][0]}',
    'Penaltis batidos' : f'{listas[11][0]}',
    'Penaltis Tentados' : f'{listas[12][0]}',
    'Cartões Amarelos' : f'{listas[13][0]}',
    'Cartões Vermelhos' : f'{listas[14][0]}',
    'Gols Esperados-xG' : f'{listas[15][0]}',
    'Gols Normais previstos-npxG' : f'{listas[16][0]}',
    'Gols assistidos esperados-xAG' : f'{listas[17][0]}',
    'Gols Esperados e gols assistidos esperados-npxG+xAG' : f'{listas[18][0]}',
    'Carregadas Progressivas' : f'{listas[19][0]}',
    'Passes Progressivos' : f'{listas[20][0]}',
    'Passes Progressivos Recebidos' : f'{listas[21][0]}',
    'Gols/90' : f'{listas[22][0]}',
    'Assis./90' : f'{listas[23][0]}',
    'Gols e Assis/90' : f'{listas[24][0]}',
    'Gols normais/90' : f'{listas[25][0]}',
    'Gols normais e assis/90' : f'{listas[26][0]}',
    'Gols Esperados-xG/90' : f'{listas[27][0]}',
    'Gols assistidos esperados-xAG/90' : f'{listas[28][0]}',
    'Gols Esperados e gols assistidos esperados-xG+xAG/90 - inc PNLT' : f'{listas[29][0]}',
    'Gols Normais previstos-npxG/90' : f'{listas[30][0]}',
    'Gols Esperados e gols assistidos esperados-npxG+xAG/90' : f'{listas[31][0]}'
    }
    
    # Escrever dados em um arquivo JSON
    with open('./james_1/Estatísticas Padrão.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)