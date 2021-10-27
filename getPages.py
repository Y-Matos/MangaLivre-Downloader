import json

def getChapterPages(info_capitulo, driver, nome_manga = 'null'):
    id_capitulo = info_capitulo['chapter_url'].split('/')[6]
    num_capitulo = info_capitulo['chapter_url'].split('/')[7]
    
    url = f'https://mangalivre.net/ler/{nome_manga}/online/{id_capitulo}/{num_capitulo}'

    print(f'Acessando {num_capitulo} | {url}')
    driver.get(url)        

    json_paginas = json.loads(driver.last_request.response.body)
    
    return json.dumps(json_paginas,ensure_ascii= False, indent=4)