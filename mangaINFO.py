import json
from createFolders import criar_nova_pasta_info
from getChapters import getChaptersFastByMangaId
from getPages import getChapterPages
from searchManga import searchMangaByName
from seleniumWebDriver import criarDriver


class manga:
    def __init__(self, /, manga_id):
        self.info = {
            "manga_id" : None,
            "manga_name" : None,
            "url_manga_name": None,
            "manga_url" : None,
            "score": None,
            "author": None,
            "artist": None,
            "cover": None,
            "manga_url": None,
            "categories": [],
            "chapter_count" : None,
            "chapters" : [],
        }
        self.get_manga_info(manga_id)
        self.get_manga_searchable_info(self.info["manga_name"])

    def get_manga_info(self, manga_id):
        json_capitulos = json.loads(getChaptersFastByMangaId(manga_id))
        self.info["manga_id"] = manga_id
        self.info["manga_name"] = json_capitulos[0]['chapter_url'].split('/')[4].replace("-"," ").title()
        self.info["url_manga_name"] = json_capitulos[0]['chapter_url'].split('/')[4]
        self.info["manga_url"] = f"https://mangalivre.net/manga/{json_capitulos[0]['chapter_url'].split('/')[4]}/{manga_id}"
        self.info["chapter_count"] = len(json_capitulos)
        self.info["chapters"] = [chapter for chapter in json_capitulos]

    def get_manga_searchable_info(self, manga_name):
        returned_info = json.loads(searchMangaByName(manga_name, exact_match=True))
        self.info["score"]= returned_info["score"]
        self.info["author"]= returned_info["author"]
        self.info["artist"]= returned_info["artist"]
        self.info["cover"]= returned_info["cover"]
        self.info["categories"]= returned_info["categories"]

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

        chapter_info["pages"] = json.loads(getChapterPages(chapter_info, criarDriver()))
        
        pasta_info = criar_nova_pasta_info(self.info["manga_name"])

        with open(f"{pasta_info}{self.info['manga_name']}_Capitulo_{chapter_info['chapter_number']}_INFO.json",'w',encoding='utf-8') as json_Manga:
            json.dump(chapter_info, json_Manga, ensure_ascii=False, indent=4)

    def print_info(self): 
        print(json.dumps(self.info, ensure_ascii=False, indent=4))

    def save_info(self):
        manga_name = self.info["manga_name"]
        pasta_info = criar_nova_pasta_info(manga_name)
        
        with open(f"{pasta_info}{self.info['manga_name']}_INFO.json",'w',encoding='utf-8') as json_Manga:
            json.dump(self.info, json_Manga, ensure_ascii=False, indent=4)
            print(f"Info.json do mangá {self.info['manga_name']} salvo com sucesso.")

    
if __name__ == '__main__':
    pass