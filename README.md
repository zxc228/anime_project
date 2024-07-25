# Anime Legends

Anime Legends - это веб-приложение на Flask, которое позволяет пользователям получать информацию о случайных аниме. 

## Требования

Для работы приложения необходимы следующие библиотеки и инструменты:

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- psycopg2-binary
- Bootstrap (для фронтенда)
- PostgreSQL

## Установка

1. Склонируйте репозиторий:

```bash
git clone https://github.com/ваш-репозиторий/anime_legends.git
cd anime_legends
```
2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # для Unix
.venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Создайте файл .env в корневом каталоге проекта и добавьте следующие переменные окружения:
```bash
DB_USER=ваш_пользователь
DB_PASSWORD=ваш_пароль
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=ваша_база_данных
SECRET_KEY=ваш_секретный_ключ
```
5. Примените миграции для создания таблиц в базе данных:
```bash
flask db upgrade
```

## Запуск
Запустите приложение командой:
```bash
python run.py
```
