import json
from getChapters import getChaptersFastByMangaId

class manga:
    def __init__(self, /, manga_id) -> json:
        self.info = {
            "manga_id" : None,
            "manga_name" : None,
            "manga_url" : None,
            "num_chapters" : None,
            "chapters" : [],
        }
        self.extract(manga_id)

    def extract(self, manga_id):
        json_capitulos = json.loads(getChaptersFastByMangaId(manga_id))
        self.info["manga_id"] = manga_id
        self.info["manga_name"] = json_capitulos[0]['Link_Capitulo'].split('/')[4]
        self.info["manga_url"] = f'https://mangalivre.net/manga/{self.info["manga_name"]}/{manga_id}'
        self.info["num_chapters"] = len(json_capitulos)
        self.info["chapters"] = [chapter for chapter in json_capitulos]

    def print(self): 
        print( json.dumps(self.info, ensure_ascii=False, indent=4))

    def saveINFO(self):
        with open(f"{self.info['manga_name']}_INFO.json",'w',encoding='utf-8') as json_Manga:
            json.dump(self.info, json_Manga, ensure_ascii=False, indent=4)
    

if __name__ == '__main__':
    one_punch = manga(1036)
    # print(one_punch)
    one_punch.saveINFO()

    one_piece = manga(13)
    one_piece.saveINFO()

    mangaAleatorio = manga(2)
    mangaAleatorio.saveINFO()
