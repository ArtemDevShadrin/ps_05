import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svetilniki"]

    def parse(self, response):
        svets = response.css('div._Ud0k')
        for svet in svets:
            yield {
                # Ссылки и теги получаем с помощью консоли на сайте
                # Создаём словарик названий, используем поиск по диву, а внутри дива — по тегу span
                'name': svet.css('div.lsooF span::text').get(),
                # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price': svet.css('div.pY3d2 span::text').get(),
                # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
                # Атрибуты — это настройки тегов
                'url': svet.css('a').attrib['href']
            }
