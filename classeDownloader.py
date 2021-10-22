import json
import requests
from requests.sessions import session
from requests_html import HTMLSession

# Baixa todas os capitulos do manga. 
def downloadChapter(json_paginas, html_session, pasta_destino):
    num_paginas = len(json_paginas['images'])
    pasta_destino = pasta_destino

    session = html_session

    for i, urls_imagem in enumerate(json_paginas['images']):
        print(f'Baixando página {i+1} de {num_paginas}')
        
        downloadPage(urls_imagem['legacy'], session, pasta_destino)
# -------------------------------------------------------------------

# Baixa todas as imagens(paginas) do capitulo. 
def downloadChapter(json_paginas, html_session, pasta_destino):
    num_paginas = len(json_paginas['images'])
    pasta_destino = pasta_destino

    session = html_session

    for i, urls_imagem in enumerate(json_paginas['images']):
        print(f'Baixando página {i+1} de {num_paginas}')
        
        downloadPage(urls_imagem['legacy'], session, pasta_destino)
# -------------------------------------------------------------------

# Baixa uma imagem da pagina 
def downloadPage(url_imagem, html_session, pasta_destino):
    pasta_destino = pasta_destino

    img = html_session.get(url_imagem)
    img_data = img.content
    
    nome_pagina = img.url.split('/')[-1]

    if str(img) == '<Response [400]>':
        print(f'Pagina com erro. Pulando...')
    else:
        with open(f'{pasta_destino}{nome_pagina}', 'wb') as handler:
            handler.write(img_data)
# -------------------------------------------------------------------