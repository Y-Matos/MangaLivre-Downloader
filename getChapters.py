from requests_html import HTMLSession
from createFolders import criar_nova_pasta_info
from getPages import getChapterPages
from seleniumWebDriver import criarDriver
import json

def getChaptersFast(url):

    session = HTMLSession()
    source = session.get(url).content
    source = session.get(url)

    script_tag = source.html.find("[src^='/mangazord_lib/js/reader.min'] + script")[0].text.strip()
    
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

def get_chapter_info(chapter_id):

    url = f"https://mangalivre.net/ler/null/online/{chapter_id}/capitulo-0/"
    
    manga_chapters = json.loads(getChaptersFast(url))
    
    chapter_index = next((index for (index, d) in enumerate(manga_chapters) if d["chapter_id"] == chapter_id), None)
    chapter = manga_chapters[chapter_index]

    chapter_info ={        
        "manga_name" : chapter["chapter_url"].split('/')[4].replace("-"," ").title(),
        "chapter_number" : chapter["chapter_number"],
        "chapter_name" : chapter["chapter_name"],
        "chapter_id" : chapter["chapter_id"],
        "chapter_url" : chapter["chapter_url"],
        "chapter_index": chapter["chapter_index"],
        "pages": []            
    }

    chapter_info["pages"] = json.loads(getChapterPages(chapter_info, criarDriver()))

    pasta_info = criar_nova_pasta_info(chapter_info["manga_name"])
    
    with open(f"{pasta_info}{chapter_info['manga_name']}_Capitulo_{chapter_info['chapter_number']}_INFO.json",'w',encoding='utf-8') as json_Manga:
        json.dump(chapter_info, json_Manga, ensure_ascii=False, indent=4)
    
    return json.dumps(chapter_info, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    pass