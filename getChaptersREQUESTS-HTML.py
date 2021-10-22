from os import link
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json
from time import perf_counter
from requests.api import options


start = perf_counter()

url = 'https://mangalivre.net/ler/one-punch-man/online/41252/capitulo-1'

session = HTMLSession()
source = session.get(url).text
soup = BeautifulSoup(source, 'html.parser')
scr = soup.find_all('script')[22].text.strip()[108:-142]

all_chapters_json = json.loads(scr)

listaCapitulos = []

for capitulo in all_chapters_json:
    for item in capitulo['releases']:
        info_capitulo = {
        "Número_Capitulo" : capitulo['number'],
        "ID_Capitulo" : capitulo['id_release'],
        "Nome_Capitulo" : capitulo['title'],
        "Link_Capitulo" : f"https://mangalivre.net{capitulo['releases'][item]['link']}"
        }
    listaCapitulos.append(info_capitulo.copy())

with open('TESTEListaCapitulosHTMLREQUESTS.txt','w',encoding='utf-8') as txt_capitulos:
    for capitulo in reversed(listaCapitulos):
        txt_capitulos.write(f"Id do Capitulo: {capitulo['ID_Capitulo']} | Link do Capitulo: {capitulo['Link_Capitulo']}\n")


end = perf_counter()
total_time = end - start
print(f'O programa demorou {total_time}s para rodar completamente.')