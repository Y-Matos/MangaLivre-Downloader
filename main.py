import json
from time import perf_counter
from mangaINFO import manga
from downloaderFunctions import downloadManga


if __name__ == '__main__':        
    start = perf_counter()

    one_punch_man = manga(1036)
    #one_punch_man.print_info()
    
    one_punch_man.get_chapter_info()
    #downloadManga(one_punch_man.info, index_inicial = 1, index_final=4)

    # one_piece = manga(3364)
    # one_piece.save_info()

    # opm = manga(1751)
    # opm.save_info()

    end = perf_counter()
    total_time = end - start
    print(f'O programa demorou {total_time}s para rodar completamente.')