
import requests
from bs4 import BeautifulSoup
import csv
CSV = 'cards.csv'
HOST = 'https://en.lyrsense.com'
URL = 'https://en.lyrsense.com/ariana_grande/last_christmas_'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r.text

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    lines_eng = []
    lines_rus = []
    eng = soup.find_all('span', class_='puzEng')
    rus = soup.select("#ru_text>span")
    for i in eng:
        i = i.text
        lines_eng.append(i)
    for i in rus:
        i = i.text
        lines_rus.append(i)

    lines = list(zip(lines_eng, lines_rus))

    # a = []
    for i in lines:
        print(f'{i[0]}\n{i[1]}')
        continue
    with open("data.txt", 'w') as song:
        for i in lines:
            song.write(f'{i[0]}\n')
            song.write(f'{i[1]}\n')

html = get_html(URL)
print(get_content(html))

    # return lines
# def save_doc(items):
#     with open("data.txt", 'w') as song:
#     for i in lines:
#         song.write(i)

# return f'{eng} \n{rus}\n {lines_eng} \n {lines_rus} \n {lines}'
# print(items)
# for item in items:
#     lines.append(
#         {
#             'eng': item.find('p', class_="hs").find("span").get("line"),
#             # 'rus': item.find('p', id_="ru_text").get('span'),
#
#         }
#     )




# def save_doc(items, path):
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(['Назв-е продукта', 'Ссылка на продукт', 'Банк', 'Изобр карты'])
#         for item in items:
#             writer.writerow([item['cards'], item['link_product'], item['brand'], item['card_img']])
#
#
# def parser(): #ф-я будет получать объект html
#     PAGENATION = input('Укажите к-во страниц для парсинга: ')
#     PAGENATION = int(PAGENATION.strip())
#
#     html = get_html(URL)
#     if html.status_code == 200:
#         cards = []
#         for page in range(1, PAGENATION):
#             print(f'Парсим страницу: {page}')
#             html = get_html(URL, params={'page': page})
#             cards.extend(get_content(html.text))
#             save_doc(cards, CSV)
#         pass
#     else:
#         print('Error')
#
#
#
# parser()
