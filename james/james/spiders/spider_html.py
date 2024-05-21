import sys
import os
import scrapy
from scrapy.crawler import CrawlerProcess

class SpiderHtmlSpider(scrapy.Spider):
    name = "spider_html"
    allowed_domains = ["fbref.com"]
    start_urls = []

    def start_requests(self):
        # Caminho para o diretório contendo os arquivos HTML
        html_dir = os.path.join(os.path.dirname(__file__))
        # Lista de arquivos HTML
        html_files = ['FBref.html']
        
        for html_file in html_files:
            file_path = os.path.join(html_dir, html_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
                yield scrapy.http.HtmlResponse(url=f'file://{file_path}', body=html_content, encoding='utf-8')

    def parse(self, response):
        # Extraia os dados desejados
        titulo = response.css('title').get()
        if titulo:
            self.log(f"{titulo}")
        else:
            self.log("Título não encontrado")

        # Exemplo de extração adicional
        # conteudo = response.xpath('//body//p/text()').getall()
        # for paragrafo in conteudo:
        #     self.log(f"Parágrafo: {paragrafo}")

process = CrawlerProcess(settings={
    "LOG_LEVEL": "DEBUG",
    # Outras configurações de Scrapy, se necessário
})

process.crawl(SpiderHtmlSpider)
process.start()