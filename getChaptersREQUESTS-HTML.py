from requests_html import HTMLSession
import json
from time import perf_counter
from getChaptersTest import getPageHTML

start = perf_counter()

#url = 'https://mangalivre.net/ler/one-punch-man/online/41252/capitulo-1#/!page0'
url = 'https://mangalivre.net/ler/one-piece/online/338197/capitulo-1029#/!page0'

def getChaptersFast(url):

    # session = HTMLSession()
    # source = session.get(url).content
    # source = session.get(url) #.content
    
    source = getPageHTML(url)
    script_tag = source.html.find('script')[22].text.strip()
    all_chapters_json = json.loads(script_tag[script_tag.find('['):script_tag.rfind(']')+1])

    lista_capitulos = []
    for capitulo in all_chapters_json:
        for item in capitulo['releases']:
            info_capitulo = {
            "Número_Capitulo" : capitulo['number'],
            "Nome_Capitulo" : capitulo['title'],
            "ID_Capitulo" : capitulo['id_release'],
            "Link_Capitulo" : f"https://mangalivre.net{capitulo['releases'][item]['link']}",
            }
        lista_capitulos.append(info_capitulo.copy())

    with open('ListaCapitulosFast.json','w',encoding='utf-8') as json_capitulos:
        json.dump(lista_capitulos[::-1], json_capitulos, ensure_ascii=False, indent=4)

    return json.dumps(lista_capitulos[::-1], ensure_ascii=False, indent=4)

def getChaptersFastByMangaId(id_manga):
    sessao = HTMLSession()
    response = sessao.get(f'https://mangalivre.net/series/chapters_list.json?page=1&id_serie={id_manga}').text
    current_page_chapters_json = json.loads(response[response.find('['):response.rfind(']')+1])

    for chapter in current_page_chapters_json[:1]:
        for item in chapter['releases']:
            url = f"https://mangalivre.net{chapter['releases'][item]['link']}"
    
    return getChaptersFast(url)

def getChaptersFull(id_manga):
    page = 1
    url = f'https://mangalivre.net/series/chapters_list.json?page={page}&id_serie={id_manga}'
    
    sessao = HTMLSession()
    response = sessao.get(url).text
    #response = getPageHTML(url).text

    lista_capitulos = []
    while response != "{\"chapters\":false}":
        current_page_chapters_json = json.loads(response[response.find('['):response.rfind(']')+1])
        
        for capitulo in current_page_chapters_json:
            for item in capitulo['releases']:
                info_capitulo = {
                "Número_Capitulo" : capitulo['number'],            
                "Nome_Capitulo" : capitulo['chapter_name'],
                "Data_Capitulo": capitulo['date'],
                "ID_Capitulo" : capitulo['id_chapter'],
                "Link_Capitulo" : f"https://mangalivre.net{capitulo['releases'][item]['link']}",
                }
            lista_capitulos.append(info_capitulo.copy())

        page += 1
        url = f'https://mangalivre.net/series/chapters_list.json?page={page}&id_serie={id_manga}'
        response = sessao.get(url).text   
    
    with open('ListaCapitulosFull.json','w',encoding='utf-8') as json_capitulos:
        json.dump(lista_capitulos[::-1], json_capitulos, ensure_ascii=False, indent=4)

    return json.dumps(lista_capitulos[::-1], ensure_ascii=False, indent=4)



#print(getChaptersFast(url))
#print(getChaptersFull(13))

print(getChaptersByMangaId(1036))

end = perf_counter()
total_time = end - start
print(f'O programa demorou {total_time}s para rodar completamente.')