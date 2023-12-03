import re

def is_valid_snils(snils):
    # Очищаем строку от лишних символов
    snils_cleaned = re.sub(r'[^0-9]', '', snils)

    # Проверяем, что длина строки после очистки равна 11
    if len(snils_cleaned) != 11:
        return False

    # Регулярное выражение для СНИЛС: три группы по три цифры, а затем две цифры
    pattern = re.compile(r'^\d{3}-\d{3}-\d{3}\s\d{2}$')

    # Проверяем соответствие строки регулярному выражению
    return bool(re.match(pattern, snils))

# Пример использования
snils_example = "123-456-789 01"
if is_valid_snils(snils_example):
    print(f"{snils_example} - корректный СНИЛС")
else:
    print(f"{snils_example} - некорректный СНИЛС")
