import scrapy
import csv


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svetilniki"]

    def parse(self, response):
        parsed_data = []
        svets = response.css('div._Ud0k')
        for svet in svets:
            try:
                name = svet.css('div.lsooF span::text').get()
                price = svet.css('div.pY3d2 span::text').get()
                url = 'https://divan.ru' + svet.css('a').attrib['href']
            except:
                print("произошла ошибка при парсинге")
                continue

            # Вносим найденную информацию в список
            parsed_data.append([name, price, url])

        with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
            # Используем модуль csv и настраиваем запись данных в виде таблицы
            # Создаём объект
            writer = csv.writer(file)
            # Создаём первый ряд
            writer.writerow(['Название', 'цена', 'ссылка'])

            # Прописываем использование списка как источника для рядов таблицы
            writer.writerows(parsed_data)
