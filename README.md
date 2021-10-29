# MangaLivre-Downloader

Meu plano é transformar isso aqui em uma api simples, mas por enquanto já funciona para baixar os capitulos dos mangas disponiveis no https://mangalivre.net/, ainda está um tanto devagar pois não comecei a transformar o código para funcionar de forma assincrona.

# Requisitos
Para utilizar a parte de informações do Manga basta instalar a biblioteca Requests-HTML. (https://github.com/psf/requests-html)

Para utilizar a parte de download e listar paginas de um capitulo é necessário também a instalação da biblioteca Selenium-Wire. (https://github.com/wkeeling/selenium-wire)

Obs.: Para o selenium wire funcionar é preciso fazer o download do ChromeDriver. (https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/). Basta baixar e colar na sua pasta C:\Program Files (x86). (Ou trocar o caminho no .py do selenium)

# Funcionalidades
  - Listar e salvar informações de um manga, incluindo o Nome, Id, Número de Capítulos, Link da Pagina do Manga, e também informações dos capitulos desse manga.

  - Listar e salvar informações de um capitulo especifico do manga, incluindo o Nome, Id, Link do Capitulo e o link para a imagem de todas as paginas do capitulo.

  - Fazer o download de capitulos de um manga.

# Como Usar?
Todo o processo pode ser feito no main.py
## Download do Manga
Por enquanto, basta criar uma instancia do manga utilizando a classe manga e então passar ela para a funcão de download, opcionalmente definindo o inicio e o fim dos capitulos a serem baixados.
```python
  one_punch_man = manga(1036) # Cria um objeto do manga passado através do ID que contém um atributo 'info' com as informações do Manga
  
  downloadManga(one_punch_man.info, index_inicial = 1, index_final=4) # Passa as informações do manga criado anteriormente, além de dois parametros opcionais definindo o inicio e o fim do download
```

## Listar ou Salvar info do Manga
Por enquanto, basta criar uma instancia do manga e printar o 'info' do mesmo. Para salvar um arquivo .Json com as informações basta utilizar o método save_info().
```python
  one_punch_man = manga(1036) # Cria um objeto do manga passado através do ID que contém um atributo 'info' com as informações do Manga
  
  one_punch_man.print_info() # Printa no console as informações do Manga
  
  one_punch_man.save_info() # Salva no arquivo .json as informações do Manga
```

# Em Breve...
