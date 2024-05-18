"""
Имеется текстовый файл file.csv, в котором разделитель полей с данными: | (верт. черта)
пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

|lastname |name |patronymic |date_of_birth |id            |
|Фамилия1 |Имя1 |Отчество1  |21.11.1998    |312040348-3048|
|Фамилия2 |Имя2 |Отчество2  |11.01.1972    |457865234-3431|

Задание
1. Реализовать сбор уникальных записей
2. Случается, что под одинаковым id присутствуют разные данные - собрать отдельно такие записи
"""

import os
import csv
from collections import defaultdict

# Путь к CSV файлу
file_path = "file.csv"

# Словарь для хранения уникальных записей
unique_records = {}
# Словарь для хранения конфликтных записей
conflicting_records = defaultdict(list)
# Словарь для хранения дубликатов
duplicate_records = defaultdict(int)


def read_from_file(file_path: str):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    with open(file_path, "r", encoding="utf-8") as file:
        return [row for row in csv.DictReader(file, delimiter="|")]


def task_1(
    file_path: str,
    unique_records: dict,
    conflicting_records: defaultdict,
    duplicate_records: defaultdict,
):
    rows = read_from_file(file_path=file_path)

    for row in rows:
        # Удаляем пробелы по краям ключей и значений
        row = {k.strip(): v.strip() for k, v in row.items()}
        record_id = row["id"]
        if record_id in unique_records:
            if unique_records[record_id] != row:
                conflicting_records[record_id].append(row)
            else:
                duplicate_records[record_id] += 1
        else:
            unique_records[record_id] = row

    # Добавляем конфликты из уникальных записей в список конфликтных записей
    for record_id, conflicts in conflicting_records.items():
        conflicts.append(unique_records.pop(record_id))

    # Убираем дубликаты, если они есть
    for record_id, count in duplicate_records.items():
        if count >= 1:
            del unique_records[record_id]

    # Вывод уникальных записей
    if not unique_records:
        print("\nУникальных записей нет")
    else:
        print("\nУникальные записи:")
        for record in unique_records.values():
            print(record)

    # Вывод конфликтных записей
    if not conflicting_records.items():
        print("\nЗаписей, где одинаковый ID и разный набор данных, нет")
    else:
        print("\nЗаписи, где одинаковый ID и разный набор данных:")
        for record_id, records in conflicting_records.items():
            print(f"\nID: {record_id}")
            for record in records:
                print(record)


if __name__ == "__main__":
    task_1(file_path, unique_records, conflicting_records, duplicate_records)
