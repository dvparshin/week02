"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

people = [
    {'name': 'Alice', 'age': 28, 'job': 'Software Developer'},
    {'name': 'Bob', 'age': 34, 'job': 'Data Analyst'},
    {'name': 'Charlie', 'age': 40, 'job': 'Project Manager'},
    {'name': 'Diana', 'age': 25, 'job': 'UI/UX Designer'}
]

def main():
    with open('export.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in people:
            writer.writerow(user)

if __name__ == "__main__":
    main()
