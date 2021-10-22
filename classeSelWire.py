from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options


#Inicia o Selenium para acessar as paginas dos capitulos retornando um webdriver.
'''class WireDriver:
    def __init__(self, headless = True):
        
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        
        self.se_wire_options = {'disable_encoding': True} # Desabilita a codificação da resposta json do servidor;
        
        self.se_options = Options()
        self.se_options.add_argument("--ignore-certificate-error")
        self.se_options.add_argument("--ignore-ssl-errors")
        self.se_options.add_argument("--log-level=3")
        self.se_options.headless = True

        self.driver = webdriver.Chrome(self.PATH, seleniumwire_options = self.se_wire_options, options= self.se_options)
        '''
def criarDriver(headless = True):
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    se_wire_options = {'disable_encoding': True} # Desabilita a codificação da resposta json do servidor;
    se_options = Options()
    se_options.add_argument("--ignore-certificate-error")
    se_options.add_argument("--ignore-ssl-errors")
    se_options.add_argument("--log-level=3")
    se_options.headless = headless

    driver = webdriver.Chrome(PATH, seleniumwire_options = se_wire_options, options= se_options)
    return driver