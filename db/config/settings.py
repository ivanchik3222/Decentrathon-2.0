import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv(dotenv_path = 'config/variables.env')
# Переменные для Telegram бота
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Переменные для PostgreSQL
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')  # По умолчанию localhost
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')  # По умолчанию 5432
POSTGRES_URL = os.getenv('POSTGRES_URL')