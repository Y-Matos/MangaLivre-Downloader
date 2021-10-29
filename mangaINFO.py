import json
import os
from getChapters import getChaptersFastByMangaId
from getPages import getChapterPages
from seleniumWebDriver import criarDriver

class manga:
    def __init__(self, /, manga_id):
        self.info = {
            "manga_id" : None,
            "manga_name" : None,
            "url_manga_name": None,
            "manga_url" : None,
            "chapter_count" : None,
            "chapters" : [],
        }
        self.get_manga_info(manga_id)

    def get_manga_info(self, manga_id):
        json_capitulos = json.loads(getChaptersFastByMangaId(manga_id))
        self.info["manga_id"] = manga_id
        self.info["manga_name"] = json_capitulos[0]['chapter_url'].split('/')[4].replace("-"," ").title()
        self.info["url_manga_name"] = json_capitulos[0]['chapter_url'].split('/')[4]
        self.info["manga_url"] = f"https://mangalivre.net/manga/{json_capitulos[0]['chapter_url'].split('/')[4]}/{manga_id}"
        self.info["chapter_count"] = len(json_capitulos)
        self.info["chapters"] = [chapter for chapter in json_capitulos]

    def get_chapter_info(self, chapter_id):
        chapter_index = next((index for (index, d) in enumerate(self.info["chapters"]) if d["chapter_id"] == chapter_id), None)
        chapter = self.info["chapters"][chapter_index]

        chapter_info ={
            "chapter_number" : chapter['chapter_number'],
            "chapter_name" : chapter['chapter_name'],
            "chapter_id" : chapter['chapter_id'],
            "chapter_url" : chapter["chapter_url"],
            "chapter_index": chapter["chapter_index"],
            "pages": []            
        }

        chapter_info["pages"] = getChapterPages(self.info["chapters"][chapter_index], criarDriver())
        
        #print(self.info["chapters"][chapter_index])
        print(json.dumps(chapter_info, ensure_ascii=False, indent=4))
        
        with open(f"{self.info['manga_name']}_{chapter_info['chapter_number']}_INFO.json",'w',encoding='utf-8') as json_Manga:
            json.dump(chapter_info, json_Manga, ensure_ascii=False, indent=4)

    def print_info(self): 
        print(json.dumps(self.info, ensure_ascii=False, indent=4))

    def save_info(self):
        pasta_atual = os.getcwd()
        pasta_info = f"{pasta_atual}\Info Mangas\\"

        try:
            os.makedirs(pasta_info)
            print(f'Pasta criada com sucesso | Caminho: {pasta_info}')
        except OSError as error:
            pass
            # print(error)
            # print("Pasta já existe, prosseguindo...")
        
        with open(f"{pasta_info}{self.info['manga_name']}_INFO.json",'w',encoding='utf-8') as json_Manga:
            json.dump(self.info, json_Manga, ensure_ascii=False, indent=4)
            print(f"Info.json do Manga {self.info['manga_name']} salvo com sucesso.")
    
if __name__ == '__main__':
    mangaAleatorio = manga(1036)
    mangaAleatorio.get_chapter_info(43700)
