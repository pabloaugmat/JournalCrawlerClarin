import shutil
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ClarinCrawler:

    def __init__(self, termo, periodo):

        self.termo = termo
        self.periodo = periodo
        self.driver = None
        self.links = {}
        self.links_filtrados = {}
        self.contador_ocorrencias = 0
        self.count = 0

    def iniciar_pesquisa(self):

        url = ("https://www.clarin.com/buscador/?q={}".format(self.termo))

        profile = webdriver.FirefoxProfile()
        profile.set_preference("javascript.enabled", True)
        self.driver = webdriver.Firefox(profile)
        self.driver.get(url)

    def raspar_paginas(self):

        paginas = self.driver.find_elements(By.CLASS_NAME, 'gsc-cursor-page')
        print(len(paginas))
        self.capturar_links()
        for n in range(1,len(paginas),1):
            print(n)
            self.capturar_links()
            paginas = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'gsc-cursor-page')))
            paginas = self.driver.find_elements(By.CLASS_NAME, 'gsc-cursor-page')
            paginas[n].click()

        self.driver.close()

    def capturar_links(self):

        carregar_noticias = WebDriverWait(self.driver, 10). \
            until(EC.presence_of_element_located((By.CLASS_NAME, 'gs-title')))

        noticias = self.driver.find_elements(By.CLASS_NAME, 'gsc-webResult')

        for noticia in noticias:
            try:
                self.links[noticia.find_element(By.TAG_NAME, 'a').get_attribute('href')] =\
                    noticia.find_element(By.CLASS_NAME, 'gs-snippet').get_attribute('textContent')
                self.count = self.count +1
                print(self.count)
            except:
                pass

        for link in self.links.keys():

            print(link)
            self.links[link] = self.links[link][:11]
            print(self.links[link])


    def filtar_links_periodo(self):

        for link in self.links:

            try:
                print(int(self.links[link][-5: ]))
                print(self.periodo['inicio'][-4:])
                if int(self.links[link][-5: ]) == int(self.periodo['inicio'][-4:]):
                    print("ok")
                    self.links_filtrados[link] = self.links[link]
    
            except:
                pass

        for link in self.links:
            print(link)

        print(self.count)