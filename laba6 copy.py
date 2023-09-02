# Функция для создания текстовой базы данных и записи данных
def zxc(database_name):
    try:
        # Создаем или открываем текстовый файл для записи
        with open(database_name, 'w') as file:
            # Записываем данные в текстовый файл
            file.write("1,Ilya,20\n")
            file.write("2,Tanya,22\n")

        print("База данных создана и заполнена данными успешно.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Функция для поиска записи по имени в текстовой базе данных
def find_record_by_name(database_name, name):
    try:
        # Открываем текстовый файл для чтения
        with open(database_name, 'r') as file:
            for line in file:
                record_id, record_name, record_age = line.strip().split(',')
                if record_name == name:
                    return int(record_id)

        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Создаем и заполняем текстовую базу данных
zxc('my_database.txt')

# Ищем запись по имени
search_name = 'Ilya'
record_id = find_record_by_name('my_database.txt', search_name)

if record_id is not None:
    print(f"Запись с именем '{search_name}' найдена. Идентификатор: {record_id}")
else:
    print(f"Запись с именем '{search_name}' не найдена.")
