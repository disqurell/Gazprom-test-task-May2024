"""
Имеется папка с файлами
Реализовать удаление файлов старше N дней
"""

import os
from datetime import datetime

folder_with_files = "."
days = -1

# Нужно, чтобы случайно не подтереть наш скрипт или другие важные файлы
exclude_deletion = [os.path.basename(__file__), "__init__.py"]


def del_old_files(path: str, days: int, exclusions: list):
    for curr_file in os.listdir(path):
        if curr_file in exclusions:
            print(f"Пропустил '{curr_file}', тк он в списке игнорируемых файлов.")
            continue

        file_path = os.path.join(path, curr_file)

        if os.path.isfile(file_path):
            file_time = os.path.getmtime(file_path)
            file_date = datetime.fromtimestamp(file_time)
            if (datetime.now() - file_date).days > days:
                os.remove(file_path)
                print(f"Уничтожил '{file_path}'")
            else:
                print(f"Проверил '{file_path}', удалять рано.")
        else:
            print(f"Пропустил '{file_path}', не файл.")


if __name__ == "__main__":
    del_old_files(path=folder_with_files, days=days, exclusions=exclude_deletion)
