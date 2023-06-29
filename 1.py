import requests
import sqlite3

# Ссылка на API
api_url = "https://api.publicapis.org/entries"

# Создание соединения с базой данных (файл будет создан, если не существует)
conn = sqlite3.connect("test_db.db")

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS api_entries (
        id INTEGER PRIMARY KEY,
        api_name TEXT,
        description TEXT,
        auth TEXT,
        https BOOLEAN,
        link TEXT,
        category TEXT
    )
''')

# Получение данных от API
response = requests.get(api_url)
data = response.json()

# Вставка данных в таблицу
for idx, entry in enumerate(data["entries"]):
    cursor.execute("INSERT INTO api_entries (id, api_name, description, auth, https, link, category) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (idx, entry["API"], entry["Description"], entry["Auth"], entry["HTTPS"], entry["Link"], entry["Category"]))

# Фиксация изменений
conn.commit()

# Закрытие соединения с базой данных
conn.close()
