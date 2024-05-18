"""
В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
Одна строка файла содержит одно слово.

Задание:
Написать программу которая выводит список слов,
каждый элемент списка которого - это новое слово,
которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
Порядок вывода слов НЕ имеет значения

Текстовый файл лежит рядом. (words.txt)

Пользователь вводит первое слово: `ласты`

Программа выводит:

ластык
ластыковка

"""

import os

file_path = "words.txt"


def read_words_from_file(file_path: str):
    if not os.path.isfile(file_path):
        print(f"Файл {file_path} не найден.")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def main(file_path: str):
    words = read_words_from_file(file_path)
    output = ""

    if not words:
        print("Файл пуст или не содержит допустимых слов.")
        return

    input_word = input("Введите первое слово: ").strip()

    if not input_word:
        print("Введено пустое слово.")
        return

    for word in words:
        if word == input_word:
            continue

        for i in range(1, len(word)):
            if input_word.endswith(word[:-i]):
                output += input_word + word[len(word) - i:] + "\n"
                break
            else:
                continue

        # Однострочник? нужен try/except на StopIteration
        # input_word += word[next(len(word) - i for i in range(1, len(word)) if input_word.endswith(word[:-i])):]
    return output


if __name__ == "__main__":
    print(main(file_path))
