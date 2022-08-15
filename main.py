from ClarinCrawler import ClarinCrawler

termos_da_pesquisa = 'haras'

periodo = {
    'inicio': '05042021',
    'fim': '30052021'
}

crawler = ClarinCrawler(termos_da_pesquisa, periodo)

crawler.iniciar_pesquisa()
crawler.raspar_paginas()
#crawler.capturar_links()
crawler.filtar_links_periodo()
