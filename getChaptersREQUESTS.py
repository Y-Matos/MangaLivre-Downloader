from bs4 import BeautifulSoup
import requests
import json
from time import perf_counter


start = perf_counter()

url = 'https://mangalivre.net/ler/one-punch-man/online/41252/capitulo-1'

source = requests.get(url).content
soup = BeautifulSoup(source, 'html.parser')
scr = soup.find_all('script')[22].text.strip()[108:-142]

all_chapters_json = json.loads(scr)

contador = 0 
listaCapitulos = []

for capitulo in all_chapters_json:
    for item in capitulo['releases']:
        #print(item)
        info_capitulo = {
        "Número_Capitulo" : capitulo['number'],
        "ID_Capitulo" : capitulo['id_release'],
        "Nome_Capitulo" : capitulo['title'],
        "Link_Capitulo" : f"https://mangalivre.net{capitulo['releases'][item]['link']}"
        }
    listaCapitulos.append(info_capitulo.copy())

with open('ListaCapitulos.txt','w',encoding='utf-8') as txt_capitulos:
    for capitulo in reversed(listaCapitulos):
        txt_capitulos.write(f"Id do Capitulo: {capitulo['ID_Capitulo']} | Link do Capitulo: {capitulo['Link_Capitulo']}\n")


end = perf_counter()
total_time = end - start
print(f'O programa demorou {total_time}s para rodar completamente.')