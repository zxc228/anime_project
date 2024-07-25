from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests
from fake_useragent import UserAgent
from models import  Anime
from . import app, db

# Настройка драйвера
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Запуск браузера в фоновом режиме
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL веб-сайта, который вы хотите парсить
url = 'https://shikimori.one/animes'

# Открываем веб-сайт
driver.get(url)

# Функция для прокрутки страницы до конца
def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Прокручиваем страницу вниз и ждем подгрузки новых данных
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    scroll_to_bottom(driver)
    time.sleep(5)  # Ожидание загрузки новых элементов
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    break

# Получаем весь HTML-код страницы
html = driver.page_source

# Закрываем драйвер
driver.quit()

# Используем BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(html, 'html.parser')

# Пример парсинга названий аниме и их ссылок
animes = []
for article in soup.select('article.c-anime'):
    title_en = article.select_one('span.name-en').get_text(strip=True)
    title_ru = article.select_one('span.name-ru').get_text(strip=True)
    link = article.select_one('a.cover')['href']

    ua = UserAgent()
    # Генерируем случайный заголовок User-Agent
    headers = {
        'User-Agent': ua.random
    }
    req = requests.get("https://shikimori.one" + link, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    # Извлекаем рейтинг
    rating_div = soup.find('div', class_='text-score')
    rating = rating_div.find('div', class_='score-value').text if rating_div else '0.0'
    rating = float(rating)

    # Извлекаем описание
    description_div = soup.find('div', class_='description-current')
    description = description_div.find('div', class_='text').text if description_div else 'No description found'

    anime = Anime(
        title_en=title_en,
        title_ru=title_ru,
        link=link,
        rating=rating,
        description=description
    )

    # Сохранение в базу данных
    with app.app_context():
        db.session.add(anime)
        db.session.commit()

    print(f'Saved: {anime}')
    time.sleep(1)

# Выводим результаты
for anime in animes:
    print(anime)
