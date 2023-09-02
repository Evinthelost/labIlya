import sqlite3


def create_and_populate_database(database_name):
    try:
        # Создаем соединение с базой данных
        conn = sqlite3.connect(database_name)

        # Создаем курсор для выполнения SQL запросов
        cursor = conn.cursor()

        # Создаем таблицу
        cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                           id INTEGER PRIMARY KEY,
                           name TEXT,
                           age INTEGER)''')

        # Вставляем данные в таблицу
        cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", ("Ilya", 20))
        cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", ("Tanya", 20))

        # Сохраняем изменения и закрываем соединение
        conn.commit()
        conn.close()
        print("База данных создана и заполнена данными успешно.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Функция для поиска записи по имени в таблице
def find_record_by_name(database_name, name):
    try:
        # Создаем соединение с базой данных
        conn = sqlite3.connect(database_name)

        # Создаем курсор для выполнения SQL запросов
        cursor = conn.cursor()

        # Выполняем SQL запрос для поиска записи
        cursor.execute("SELECT id FROM my_table WHERE name = ?", (name,))

        # Извлекаем результат запроса
        result = cursor.fetchone()

        # Закрываем соединение с базой данных
        conn.close()

        # Если найдена запись, возвращаем ее идентификатор, иначе возвращаем None
        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Создаем и заполняем базу данных
create_and_populate_database('my_database.db')

# Ищем запись по имени
search_name = 'Ilya'
record_id = find_record_by_name('my_database.db', search_name)

if record_id is not None:
    print(f"Запись с именем '{search_name}' найдена. Идентификатор: {record_id}")
else:
    print(f"Запись с именем '{search_name}' не найдена.")
