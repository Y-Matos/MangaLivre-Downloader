from os import getcwd, makedirs

# Checa e cria pasta para armazenar as informações dos capitulos e/ou mangas 
def criar_nova_pasta_info(nome_manga):
    
    pasta_atual = getcwd()
    pasta_info = f'{pasta_atual}\Info Mangas\{nome_manga}\\'

    try:
        makedirs(pasta_info)
        print(f'Pasta criada com sucesso | Caminho: {pasta_info}')
    except OSError as error:
        pass
        #print(error)
    
    return pasta_info 

# Checa e cria pasta para armazenar as paginas baixadas do capitulo 
def criar_nova_pasta_manga(nome_manga, num_capitulo):
    
    pasta_atual = getcwd()
    nova_pasta = f'{pasta_atual}\{nome_manga}\{num_capitulo}\\'

    try:
        makedirs(nova_pasta)
        print(f'Pasta {num_capitulo} criada com sucesso | Caminho: {nova_pasta}')
    except OSError as error:
        print(error)
    
    return nova_pasta      

# -------------------------------------------------------------------