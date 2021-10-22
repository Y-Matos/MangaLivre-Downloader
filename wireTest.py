import requests
import json
import time
import os
from requests_html import HTMLSession
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from classeSelWire import criarDriver 
from classeDownloader import downloadChapter

# https://github.com/iShi0n/mangalivre-api
# https://github.com/Marcelo-maga/manga-download
# https://github.com/AbbadB/MangaScraping-MangaLivre
# https://github.com/Claus-Alberto/Manga_Collector

total_start = time.perf_counter()

#driver = WireDriver(headless=False)
driver = criarDriver(headless=True)

with open('ListaCapitulos.txt','r',encoding='utf-8') as txt_capitulos:

    payload = ""
    headers = {
        "authority": "mangalivre.net",
        "sec-ch-ua": "^\^Chromium^^;v=^\^94^^, ^\^Google",
        "User-Agent": "Mozilla/5.0"
    }

    lista_capitulos = [(linha[:-1].split(',')) for linha in txt_capitulos]

    for capitulo in lista_capitulos[2:5]:        
        chapter_start = time.perf_counter()
        link_capitulo = capitulo[1]
        num_capitulo = link_capitulo.split('/')[6]
        nome_capitulo = link_capitulo.split('/')[7]
        
        url = f'https://mangalivre.net/ler/one-punch-man/online/{num_capitulo}/{nome_capitulo}#/!page0'
        print(f'Acessando {nome_capitulo}, {url}')

        driver.scopes = [f'.*https://mangalivre.net/leitor/pages/{num_capitulo}.json*']
        driver.get(url)
        

        pages_links = json.loads(driver.last_request.response.body)

        #for pagina in json_response['images']:
        #    print(pagina['legacy'])
        

        
    # Checa e cria pasta para armazenar as paginas baixadas do capitulo 
        pasta_atual = os.getcwd()
        nova_pasta = f'{pasta_atual}\{nome_capitulo}\\'

        try:
            os.mkdir(nova_pasta)
            print(f'Pasta {nome_capitulo} criada com sucesso. Path: {nova_pasta}')
        except OSError as error:
            print(error)
    # -------------------------------------------------------------------
    
    # Baixa todas as imagens(paginas) do capitulo. 
        dcap = time.perf_counter()
        session = HTMLSession()
        downloadChapter(pages_links, session, nova_pasta)
        fdcap = time.perf_counter()
        print(f'Tempo baixando o capitulo: {fdcap-dcap}')
    # -------------------------------------------------------------------
        
        chapter_end = time.perf_counter()
        chapter_time = chapter_end - chapter_start
        print(f'O capitulo demorou {chapter_time}s para obter as paginas.')
       
driver.close()
total_end = time.perf_counter()
total_time = chapter_end - total_start
print(f'O script demorou {total_time}s para rodar completamente.')