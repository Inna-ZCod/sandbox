# 1. Удалить из стартовой строки пробелы и знаки препинания и привести строку к нижнему регистру:
#   - создать таблицу перевода, содержащую символы, которые нужно удалить
#   - удалить лишние символы и привести строку к нижнему регистру
#
# 2. Определить длину строки
#
# 3. Пройти по строке от начала до середины с помощью цикла for
#
# 4. Сравнить символы первой половины с символами второй половины строки
#
# 5. Если на одной из итераций цикла символы не совпадут, вернуть False, иначе - True


import string

def is_palindrome(s):
    # Создаем таблицу перевода, чтобы убрать знаки препинания
    table = str.maketrans('', '', string.punctuation + ' ')

    # Удаляем знаки препинания и приводим строку к нижнему регистру
    s = s.translate(table).lower()

    # Длина строки
    n = len(s)

    # Проходим по половине строки
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False

    # Если все символы совпали, строка является палиндромом
    return True


# Пример использования
example_string = "Кукарямба"

result = is_palindrome(example_string)

if result:
    print(f"Строка '{example_string}' является палиндромом")
else:
    print(f"Строка '{example_string}' не является палиндромом")