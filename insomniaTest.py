import requests
import json
import time
import os
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

total_start = time.perf_counter()
with open('ListaCapitulos.txt','r',encoding='utf-8') as txt_capitulos:

    payload = ""
    headers = {
        "authority": "mangalivre.net",
        "sec-ch-ua": "^\^Chromium^^;v=^\^94^^, ^\^Google",
        "User-Agent": "Mozilla/5.0"
    }

    lista_capitulos = [(linha[:-1].split(',')) for linha in txt_capitulos]
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = Options()
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--log-level=3")
    options.headless = True
    driver = webdriver.Chrome(PATH, options=options)
    
    #driver.request_interceptor = interceptor
    

    for capitulo in lista_capitulos[:2]:
        chapter_start = time.perf_counter()
        link_capitulo = capitulo[1]
        num_capitulo = link_capitulo.split('/')[6]
        nome_capitulo = link_capitulo.split('/')[7]
        
        url = f'https://mangalivre.net/ler/one-punch-man/online/{num_capitulo}/{nome_capitulo}'
        print(f'Acessando {nome_capitulo}, {url}')
        
        # resposta = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

        # session = HTMLSession()
        # r = session.get(url)
        # r.html.render()

        # resposta = r.request.headers
        
        # PATH = "C:\Program Files (x86)\chromedriver.exe"
        # options = Options()
        # options.add_argument("--ignore-certificate-error")
        # options.add_argument("--ignore-ssl-errors")
        # options.headless = False
        # driver = webdriver.Chrome(PATH, options=options)
        
        driver.scopes = [f'.*https://mangalivre.net/leitor/pages/{num_capitulo}.json*']
        
        driver.get(url)
        
        api_key = driver.last_request.url.split('=')[1]
        print(api_key)

        

        url = f"https://mangalivre.net/leitor/pages/{num_capitulo}.json"

        querystring = {"key":f'{api_key}'}

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        response_json = response.json()
        for pagina in response_json['images']:
            print(pagina['legacy'])
        num_paginas = len(response_json['images'])
        print(f'{nome_capitulo} tem {num_paginas} paginas.')
        
        # pagina0 = requests.get(response_json['images'][0])
        # nome_pagina = pagina0.url.split('/')[-1]
        # print(nome_pagina)
        # if str(pagina0) == '<Response [400]>':
        #     print(f'Pagina com erro. Pulando...')

        '''print(f'{nome_capitulo} tem {num_paginas} paginas.')

        pasta_atual = os.getcwd()
        nova_pasta = f'{pasta_atual}\{nome_capitulo}\\'

        try:
            os.mkdir(nova_pasta)
            print(f'Pasta {nome_capitulo} criada com sucesso. Path: {nova_pasta}')
        except OSError as error:
            print(error)

        for i, url_imagem in enumerate(response_json['images']):
            print(f'Baixando página {i+1} de {num_paginas}')
            print(url_imagem)
            img = requests.get(url_imagem)
            nome_pagina = img.url.split('/')[-1]
            img_data = img.content
            if str(img) == '<Response [400]>':
                print(f'Pagina {i+1} com erro. Pulando...')
            else:
                with open(f'{nova_pasta}{nome_pagina}', 'wb') as handler:
                    handler.write(img_data)'''
        
        chapter_end = time.perf_counter()
        chapter_time = chapter_end - chapter_start
        print(f'O capitulo demorou {chapter_time}s para obter as paginas.')
    
driver.close()
total_end = time.perf_counter()
total_time = chapter_end - total_start
print(f'O script demorou {total_time}s para rodar completamente.')