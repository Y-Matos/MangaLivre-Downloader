import json
from time import perf_counter
from requests_html import HTMLSession
from createFolders import criar_nova_pasta_manga
from seleniumWebDriver import criarDriver
from getPages import getChapterPages

# Baixa todos os capitulos do manga (Se não for passada um capitulo final). 
def downloadManga(manga_info, index_inicial = 1, index_final = None): 
    driver = criarDriver()
    session = HTMLSession()

    nome_manga = manga_info["manga_name"]
    nome_manga_url = manga_info["url_manga_name"]


    for capitulo in manga_info["chapters"][index_inicial-1:index_final]:
        num_capitulo = capitulo['chapter_url'].split('/')[7]

        json_paginas = json.loads(getChapterPages(capitulo, driver, nome_manga_url))

        pasta_capitulo = criar_nova_pasta_manga(nome_manga,num_capitulo)

        downloadChapter(json_paginas, session, pasta_capitulo)
    
    driver.close()
# -------------------------------------------------------------------

# Baixa todas as imagens(paginas) do capitulo. #!!!!!!!!!!!!!!!!!!!!!!!!! Adicionar uma forma de escolher baixar .avif ou .png
def downloadChapter(json_paginas, html_session, pasta_destino):
    start = perf_counter()        
    
    num_paginas = len(json_paginas['images'])

    for i, urls_imagem in enumerate(json_paginas['images']):
        print(f'Baixando página {i+1} de {num_paginas}')        
        downloadPage(urls_imagem['avif'], html_session, pasta_destino)
    
    end = perf_counter()
    print(f'Tempo baixando o capitulo: { end - start }s')
# -------------------------------------------------------------------

# Baixa uma imagem da pagina 
def downloadPage(url_imagem, html_session, pasta_destino):
    img_response = html_session.get(url_imagem)
    img_data = img_response.content
    
    nome_pagina = img_response.url.split('/')[-1]

    if img_response.status_code == 400:
        print(f'Pagina com erro. Pulando...')
    else:
        with open(f'{pasta_destino}{nome_pagina}', 'wb') as handler:
            handler.write(img_data)
# -------------------------------------------------------------------

if __name__ == "__main__":
    pass