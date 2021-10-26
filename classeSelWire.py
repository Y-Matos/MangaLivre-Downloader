from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

#Inicia o Selenium-Wire para acessar as paginas dos capitulos retornando um webdriver.
def criarDriver(headless = True):
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    se_wire_options = {'disable_encoding': True} # Desabilita a codificação da resposta json do servidor;
    se_options = Options()
    se_options.add_argument("--ignore-certificate-error")
    se_options.add_argument("--ignore-ssl-errors")
    se_options.add_argument("--log-level=3")
    se_options.headless = headless

    driver = webdriver.Chrome(PATH, seleniumwire_options = se_wire_options, options= se_options)
    driver.scopes = [f'.*https://mangalivre.net/leitor/pages.*.json*']
    return driver