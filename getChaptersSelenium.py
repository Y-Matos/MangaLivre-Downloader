from bs4 import BeautifulSoup
import requests
import time
from requests.api import options
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

def get_page_img_url(page_url : str, driver: webdriver) -> str :
    driver.get(page_url)
    driver.refresh()
    try:
        link_img_pagina = str(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH , '/html/body/div[2]/div[5]/div[3]/div[2]/div[1]/img'))
        ).get_attribute('src')) + '\n'

        return link_img_pagina
    except StaleElementReferenceException:
        get_page_img_url(page_url,driver)

    #return get_page_img_url(page_url, driver)

start = time.time()

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
options.headless = False
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://mangalivre.net/manga/one-punch-man/1036')

check_height = driver.execute_script("return document.body.scrollHeight;") 
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    height = driver.execute_script("return document.body.scrollHeight;") 
    if height == check_height: 
        break 
    check_height = height

try:
    chapters = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "chapter-list"))
    )
except:
    driver.quit()

capitulos = chapters.find_elements_by_class_name('link-dark')

end = time.time()

with open('ListaCapitulos','w',encoding='utf-8') as txt_capitulos:
    for capitulo in reversed(capitulos):
        nome_capitulo = capitulo.find_element_by_class_name('cap-text')
        link_capitulo = capitulo.get_attribute('href')
        info_capitulo = f'{nome_capitulo.text},{link_capitulo}\n'
        txt_capitulos.write(info_capitulo)


total_time = end - start
print(f'O programa demorou {total_time}s para rodar completamente.')  # 12.26 segundos

'''for capitulo in capitulos:
    nome_capitulo = capitulo.find_element_by_class_name('cap-text')
    link_capitulo = capitulo.get_attribute('href')
    print(nome_capitulo.text, "Link:", link_capitulo)

    driver.get(link_capitulo)

    paginas = driver.find_element_by_class_name('page-navigation')
    pagina_atual = int(paginas.find_elements_by_tag_name('em')[0].text)-1
    numero_de_paginas = int(paginas.find_elements_by_tag_name('em')[1].text)

    print(paginas.text, "Pagina Atual:", pagina_atual, numero_de_paginas)

    # link_pagina = 'link_capitulo' + '#/!page' + str(pagina_atual)
    # print(link_pagina)
    # driver.get(link_pagina)

    # box_pagina_manga = driver.find_element_by_class_name('manga-image')

    # print(box_pagina_manga)

    # src_pagina_manga = box_pagina_manga.find_element_by_tag_name('img').get_attribute('src')
    # print(src_pagina_manga)'''





# with open('ListaCapitulos','r',encoding='utf-8') as txt_capitulos:

#     lista_capitulos = [(linha[:-1].split(',')) for linha in txt_capitulos]

#     for capitulo in lista_capitulos[:1]:
#         link_capitulo = capitulo[1]
#         print(capitulo[0], "Link:", link_capitulo)

#         driver.get(link_capitulo)

#         paginas = driver.find_element_by_class_name('page-navigation')
#         pagina_atual = int(paginas.find_elements_by_tag_name('em')[0].text)-1
#         numero_de_paginas = int(paginas.find_elements_by_tag_name('em')[1].text)

#         start = time.time()
#         with open('links_paginas','w',encoding='utf-8') as links_paginas:
            
#             for pagina in range(numero_de_paginas):
#                 link_pagina = f'{link_capitulo}#/!page{str(pagina)}'
#                 print(link_pagina)

#                 link_img_pagina = get_page_img_url(link_pagina, driver)
#                 # driver.get(link_pagina)
#                 # driver.refresh()
                
#                 # # manga_image = driver.find_element_by_class_name('manga-image')
#                 # # link_img_pagina = manga_image.find_element_by_tag_name('img').get_attribute('src')
#                 # link_img_pagina = str(WebDriverWait(driver, 10).until(
#                 #     EC.presence_of_element_located((By.XPATH , '/html/body/div[2]/div[5]/div[3]/div[2]/div[1]/img'))
#                 #     ).get_attribute('src')) + '\n'
#                 # #link_img_pagina = driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div[2]/div[1]/img').get_attribute('src')
#                 print(link_img_pagina)
#                 links_paginas.write(link_img_pagina)

#                 #time.sleep(1)

#         end = time.time()
#         total_time = end - start
#         print(f'O programa demorou {total_time}s para rodar completamente.')
#         # driver.get(link_pagina)

#     # box_pagina_manga = driver.find_element_by_class_name('manga-image')

#     # print(box_pagina_manga)

#     # src_pagina_manga = box_pagina_manga.find_element_by_tag_name('img').get_attribute('src')
#     # print(src_pagina_manga)'''



# # with open('ListaCapitulos','r',encoding='utf-8') as txt_capitulos:

# #     lista_links = [linha[:-1].split(',')[1] for linha in txt_capitulos]
    
# #     for link in lista_links[:1]:
# #         print(link)

# #         source = requests.get(link,headers={'User-Agent': 'Mozilla/5.0'}).text
# #         soup = BeautifulSoup(source,'lxml')
# #         #print(soup.prettify())

# #         num_paginas = soup.find('reader-total-pages')
# #         print(num_paginas)

# #         manga_image = soup.find('div', class_='manga-image')
# #         link_img_pagina = manga_image.find('img')['src']

# #         print(link_img_pagina)

# #         time.sleep(1)

driver.quit()