import json
from time import perf_counter
from mangaINFO import manga
from searchManga import searchMangaByName, get_manga_id_by_name
from downloaderFunctions import downloadManga
from getChapters import get_chapter_info


if __name__ == '__main__':        
    start = perf_counter()

    #one_punch_man = manga(1036)
    #one_punch_man.get_chapter_info(41252)
    #one_punch_man.save_info()

    get_chapter_info(327108)

    #downloadManga(one_punch_man.info, index_inicial = 1, index_final=4)

    #print(searchMangaByName("one piece ", exact_match=True))

    end = perf_counter()
    total_time = end - start
    print(f'O programa demorou {total_time}s para rodar completamente.')