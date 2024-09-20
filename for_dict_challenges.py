# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_count = {}

# Подсчет повторений имен
for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1  # если имя уже есть в словаре, увеличиваем счетчик
    else:
        name_count[name] = 1  # если имени нет, добавляем его с начальным значением 1

# Вывод количества повторений каждого имени
for name, count in name_count.items():
    print(f"{name}: {count}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_count = {}

# Подсчет повторений имен
for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1  # если имя уже есть в словаре, увеличиваем счетчик
    else:
        name_count[name] = 1  # если имени нет, добавляем его с начальным значением 1

max_key = max(name_count, key=name_count.get)
print(f"Самое частое имя среди учеников: {max_key}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
def find_frequent_name(students):
    name_count = {}
    for student in students:
        name = student['first_name']
        if name in name_count:
            name_count[name] += 1  # если имя уже есть в словаре, увеличиваем счетчик
        else:
            name_count[name] = 1  # если имени нет, добавляем его с начальным значением 1
    frequent_name = max(name_count, key=name_count.get)
    return frequent_name

# Вывод самого частого имени в каждом классе
for class_number, students in enumerate(school_students, start=1):
    frequent_name = find_frequent_name(students)
    print(f"Самое частое имя в классе {class_number}: {frequent_name}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for class_info in school:
    class_name = class_info['class']
    students = class_info['students']

    boys_count = 0
    girls_count = 0

    # Подсчет количества мальчиков и девочек
    for student in students:
        name = student['first_name']
        if is_male.get(name):  # если is_male[name] == True, это мальчик
            boys_count += 1
        else:
            girls_count += 1

    # Вывод результатов
    print(f"Класс {class_name}: девочки {girls_count}, мальчики {boys_count}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
max_boys = 0
max_girls = 0
class_with_max_boys = ""
class_with_max_girls = ""

for class_info in school:
    class_name = class_info['class']
    students = class_info['students']

    boys_count = 0
    girls_count = 0

    # Подсчет количества мальчиков и девочек
    for student in students:
        name = student['first_name']
        if is_male.get(name):  # если is_male[name] == True, это мальчик
            boys_count += 1
        else:
            girls_count += 1

    # Проверяем, является ли этот класс рекордсменом по количеству мальчиков
    if boys_count > max_boys:
        max_boys = boys_count
        class_with_max_boys = class_name
    
    # Проверяем, является ли этот класс рекордсменом по количеству девочек
    if girls_count > max_girls:
        max_girls = girls_count
        class_with_max_girls = class_name

# Вывод результатов
print(f"Больше всего мальчиков в классе {class_with_max_boys}")
print(f"Больше всего девочек в классе {class_with_max_girls}")

