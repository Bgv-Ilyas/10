# Ввод строк с клавиатуры
line1 = input("Введите первую строку: ")
line2 = input("Введите вторую строку: ")

# Преобразование строк в множества символов
variety1 = set(line1)
variety2 = set(line2)

# Находим общие символы
common_characters = variety1.intersection(variety2)

# Вывод результата
print("Общие символы в двух строках:", common_characters)
