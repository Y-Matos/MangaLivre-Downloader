from requests_html import HTMLSession
import json

def getChaptersFast(url):

    session = HTMLSession()
    source = session.get(url).content
    source = session.get(url) #.content
    
    script_tag = source.html.find("[src^='/mangazord_lib/js/reader.min'] + script")[0].text.strip()
    

    #script_tag = source.html.find('script')[22].text.strip()
    all_chapters_json = json.loads(script_tag[script_tag.find('['):script_tag.rfind(']')+1])

    lista_capitulos = []
    for index, capitulo in enumerate(reversed(all_chapters_json)):
        for item in capitulo['releases']:
            info_capitulo = {
            "chapter_number" : capitulo['number'],
            "chapter_name" : capitulo['title'],
            "chapter_id" : capitulo['id_release'],
            "chapter_url" : f"https://mangalivre.net{capitulo['releases'][item]['link']}",
            "chapter_index": index+1
            }
        lista_capitulos.append(info_capitulo.copy())

    #with open('ListaCapitulosFast.json','w',encoding='utf-8') as json_capitulos:
    #    json.dump(lista_capitulos[::1], json_capitulos, ensure_ascii=False, indent=4)

    return json.dumps(lista_capitulos[::1], ensure_ascii=False, indent=4)   # Retornar JSON OU STRING ????

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

    lista_capitulos = []
    while response != "{\"chapters\":false}":
        current_page_chapters_json = json.loads(response[response.find('['):response.rfind(']')+1])
        
        for index, capitulo in enumerate(reversed(current_page_chapters_json)):
            for item in capitulo['releases']:
                info_capitulo = {
                "Número_Capitulo" : capitulo['number'],            
                "Nome_Capitulo" : capitulo['chapter_name'],
                "Data_Capitulo": capitulo['date'],
                "ID_Capitulo" : capitulo['id_chapter'],
                "Link_Capitulo" : f"https://mangalivre.net{capitulo['releases'][item]['link']}",
                "chapter_index" : index+1,
                }
            lista_capitulos.append(info_capitulo.copy())

        page += 1
        url = f'https://mangalivre.net/series/chapters_list.json?page={page}&id_serie={id_manga}'
        response = sessao.get(url).text   
    
    #with open('ListaCapitulosFull.json','w',encoding='utf-8') as json_capitulos:
    #    json.dump(lista_capitulos[::1], json_capitulos, ensure_ascii=False, indent=4)

    return json.dumps(lista_capitulos[::1], ensure_ascii=False, indent=4)

if __name__ == '__main__':
    pass