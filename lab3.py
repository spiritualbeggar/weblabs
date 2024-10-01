a = input("введите целые числа")
a = a.split()
print(a)

a = (input("\введите названия городов\n"))
a = a.split()
b = (input("\введите исходный город\n"))
print(b in a)


cities_input = input("Введите названия городов через пробел: ")
cities_list = cities_input.split()
print("Последний город в списке:", cities_list[-1])



grades_input = input("Введите оценки студента (от 0 до 5) через пробел: ")
grades_list = list(map(int, grades_input.split()))
average_grade = sum(grades_list) / len(grades_list)
print(f"Средний балл: {average_grade:.1f}")


subscribers_input = input("Введите число новых подписчиков по дням: ")
subscribers_list = list(map(int, subscribers_input.split()))
max_subscribers = max(subscribers_list)
min_subscribers = min(subscribers_list)
total_subscribers = sum(subscribers_list)
print(max_subscribers, min_subscribers, total_subscribers)

data = input("Введите имя, отчество и фамилию через пробел: ")
print(f"{data.split()[2]} {data.split()[1][0]}.{data.split()[0][0]}.")

cities = ["Москва", "Тверь", "Вологда"]
new_cities_input = input("Введите названия городов через пробел: ")
new_cities = new_cities_input.split()
cities.extend(new_cities)
print(*cities)

cities = ["Москва", "Тверь", "Вологда"]
new_cities_input = input("Введите названия городов через пробел: ")
new_cities = new_cities_input.split()
cities = new_cities + cities
print(*cities)

views_input = input("Введите числа просмотров видео по дням через пробел: ")
views = list(map(int, views_input.split()))
first_three_views = views[:3]
print("Первые три значения просмотров:", *first_three_views)

views_input = input("Введите числа просмотров видео по дням через пробел: ")
views = list(map(int, views_input.split()))
last_four_views = views[-4:]
print("Последние четыре значения просмотров:", *last_four_views)

cities_input = input("Введите названия городов через пробел: ")
cities = cities_input.split()
every_second_city = cities[::2]
print("Города через один (начиная с первого):", *every_second_city)

cities_input = input("Введите названия городов через пробел: ")
cities = cities_input.split()
every_second_city = cities[1::2]
print("Города через один (начиная со второго):", *every_second_city)

grades_input = input("Введите оценки студента через пробел (не менее 10 оценок): ")
grades = list(map(int, grades_input.split()))
selected_grades = grades[2:7]
reversed_grades = selected_grades[::-1]
print("Оценки с 3-го по 7-й в обратном порядке:", *reversed_grades)

grades_input = input("Введите оценки студента через пробел (не менее 10 оценок): ")
grades = list(map(int, grades_input.split()))
selected_grades = grades[-1::-2]  
reversed_grades = selected_grades[::-1]
print("Оценки через один, начиная с последнего, в обратном порядке:", *reversed_grades)

numbers_input = input("Введите целые числа через пробел: ")
numbers = list(map(int, numbers_input.split()))
result = numbers + [numbers[0] != numbers[-1]]
print(*result)

cities_input = input("Введите названия городов через пробел: ")
cities = cities_input.split()
new_city = input("Введите название нового города: ")
cities.insert(1, new_city)
print(*cities)

title = input("Введите название книги: ")
author = input("Введите автора книги: ")
pages = int(input("Введите число страниц: "))
price = float(input("Введите цену книги: "))
book_info = [title, author, pages, price]
book_info.pop(2)
book_info[1] = "Пушкин"
book_info[2] *= 2
print("Обновленная информация о книге:")
print(f"Название: {book_info[0]}")
print(f"Автор: {book_info[1]}")
print(f"Цена: {book_info[2]:.2f}")  

subscribers_input = input("Введите число новых подписчиков по дням через пробел: ")
subscribers_list = list(map(int, subscribers_input.split()))
subscribers_list.sort(reverse=True)
print("Отсортированный список новых подписчиков по убыванию:")
print(subscribers_list)
phone_number = input("Введите номер телефона: ")
phone_list = list(phone_number)
if phone_list[0] == '+':
    phone_list.pop(0)
for i in range(len(phone_list)):
    if phone_list[i] == '7':
        phone_list[i] = '8'
phone_list = [char for char in phone_list if char != '-']
formatted_phone_number = ''.join(phone_list)
print("Преобразованный номер телефона:", formatted_phone_number)

numbers = list(map(int, input("Введите целые числа через пробел (не менее четырех): ").split()))
min1 = float('inf')
min2 = float('inf')
min3 = float('inf')
for num in numbers:
    if num < min1:
         min3 = min2
         min2 = min1
         min1 = num
    elif num < min2:
        min3 = min2
        min2 = num
    elif num < min3:
        min3 = num
    result = [min1, min2, min3]
    result.sort()
    print("Три наименьших числа:", result)

numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
last_value = numbers.pop()
numbers.append((last_value % 2) == 1)
print(*numbers)

grades = list(map(int, input("Введите оценки студента через пробел (не менее 8): ").split()))
count_of_twos = grades.count(2)
print("Количество двоек:", count_of_twos)

rivers = input("Введите названия рек через пробел: ").split()
sorted_rivers = sorted(rivers)
if sorted_rivers:
    sorted_rivers.pop(0)
print(" ".join(sorted_rivers))

float_numbers = input("Введите числа с плавающей точкой: ").split()
float_list = [float(num) for num in float_numbers]
int_numbers = input("Введите целые числа: ").split()
int_list = [int(num) for num in int_numbers]
float_list.append(int_list)
print("Результирующий список:", float_list)

poem = []
for i in range(3):
    line = input(f"Введите строку {i + 1} стихотворения: ")
    poem.append(line.split())
print("Результирующий вложенный список:")
print(poem)

matrix = []
for i in range(3):
    line = input(f"Введите строку {i + 1} матрицы (числа через пробел): ")
    matrix.append(line.split())
last_column = [row[-1] for row in matrix]
result = ' '.join(last_column)
print("Последний столбец матрицы:", result)

