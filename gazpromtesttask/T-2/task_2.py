"""
В наличии список множеств. внутри множества целые числа

m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

Задание: посчитать
1. общее количество чисел
2. общую сумму чисел
3. посчитать среднее значение
4. собрать все множества в один кортеж
написать решения в одну строку
"""

m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]


class SecondTask:
    def __init__(self, input_data: list):
        self.input_data = input_data

    @property
    def numbers_count(self):
        """Возвращает общее количество чисел в списке"""
        return sum([len(i) for i in self.input_data])

    @property
    def sum_numbers(self):
        """Возвращает сумму чисел"""
        return sum([sum(i) for i in self.input_data])

    @property
    def average_numbers(self):
        """Возвращает среднее значение"""
        return self.sum_numbers / self.numbers_count

    @property
    def to_one_tuple(self):
        """Собирает все множества в один кортеж"""
        return tuple(element for subset in self.input_data for element in subset)


if __name__ == "__main__":
    task = SecondTask(m)

    print(f"Количество чисел:           {task.numbers_count}")
    print(f"Сумма чисел:                {task.sum_numbers}")
    print(f"Среднее значение:           {task.average_numbers}")
    print(f"Все мно-ва в одном кортеже: {task.to_one_tuple}")
