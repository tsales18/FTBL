import scrapy
from scrapy.crawler import CrawlerProcess
class MeuSpider(scrapy.Spider):
    name = 'james_spdr'
    allowed_domains = ['flashscore.com.br']
    start_urls = ['https://www.flashscore.com.br/futebol/brasil/brasileirao-betano/#/Klz7n21m/table/overall']

    def parse(self, response):
        # Extraia os dados desejados
        titulo = response.css('title::text').get()
        if titulo:
            self.log(f"{titulo}")
        else:
            self.log("Título não encontrado")
        
        # Ou você pode usar CSS selectors
        # 
        # if titulo:
        #     self.log(f"Título da página: {titulo}")
        # else:
        #     self.log("Título não encontrado")

process = CrawlerProcess(settings={
    "LOG_LEVEL": "DEBUG",
    # Outras configurações de Scrapy, se necessário
})

process.crawl(MeuSpider)
process.start()