# Telegram-бот для обмена криптоволютой.
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Описание проекта:
Бот служит для обмена криптовалютой из рубли в BTC, ETH, SOL и обратно. Бот работает с платежной системой QIWI и API Binance. Так же в боте реализована Админ панель, ведутся логи , сделана локализация для иностранных пользователей и реферальная система.

## Настройки:

Для запуска бота нужно создать файл .env и указать: <br>
BOT_TOKEN - токен telegram-bot <br>
API_KEY - токен API Binance <br>
API_SECRET - секретный ключь API Binance <br>
PGUSER - юзернейм/логин от базы данных PostgreSQL <br>
PGPASSWORD - пароль от базы данных PostgreSQL <br>
DATABASE - название базы данных <br>
QIWI_TOKEN - токен QIWI <br>
WALLET_QIWI - номер кошелька QIWI <br>
QIWI_PUBKEY - публичный ключь киви <br>

```python
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
API_KEY = str(os.getenv("API_KEY"))
API_SECRET = str(os.getenv("API_SECRET"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
QIWI_TOKEN = str(os.getenv("qiwi"))
WALLET_QIWI = str(os.getenv("wallet"))
QIWI_PUBKEY = str(os.getenv("qiwi_p_pub"))
```
Так же для управления ботом указать свой чат ID в файле config.py
```python
admins = [
    #ваш чат id
]
```

Для настройки перевода необходимо перейти в файл Languages instruction, там описана подробная инструкция

## Запуск проекта

Клонируйте репозиторий: 
 
``` 
https://github.com/emuhich/CryptoBot.git
``` 

Перейдите в папку проекта в командной строке:

``` 
cd CryptoBot
``` 

Создайте и активируйте виртуальное окружение:

``` 
python -m venv venv
``` 
``` 
venv/Scripts/activate
``` 

Установите зависимости из файла *requirements.txt*: 
 
``` 
pip install -r requirements.txt
``` 
Запустите сервер:
``` 
python app.py
``` 
