"""
Имеется список списков
a = [[1,2,3], [4,5,6]]

Задание:
Сделать список словарей

b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
написать решение в одну строку
"""

a = [[1, 2, 3], [4, 5, 6]]


def list_dict(input_data: list):
    return [dict(zip([f"k{j+1}" for j in range(len(i))], i)) for i in input_data]


if __name__ == "__main__":
    print(list_dict(a))
