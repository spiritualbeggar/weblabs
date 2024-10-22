print("Задание 9.1.")
def my_first_function():
    print("It's my first function")

my_first_function()
print("Задание 9.2.")
def greet_user():
    name, surname = input("Введите имя и фамилию через пробел: ").split()
    print(f"Уважаемый, {name} {surname}! Вы верно выполнили это задание!")

greet_user()
def print_weight(weight):
    print(f"Предмет имеет вес: {weight} кг.")

x = float(input("Введите вес предмета: "))
def print_weight(weight):
    print(f"Предмет имеет вес: {weight} кг.")
print_weight(x)
def analyze_list(lst):
    v_min = min(lst)
    v_max = max(lst)
    v_sum = sum(lst)
    print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")

lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))
analyze_list(lst)
def print_perimeter(width, height):
    perimeter = 2 * (width + height)
    print(f"Периметр прямоугольника, равен {perimeter}")

width, height = map(int, input("Введите ширину и высоту прямоугольника через пробел: ").split())
print_perimeter(width, height)
def check_email(email):
    if '@' in email and '.' in email and all(c.isalnum() or c in '_.' for c in email):
        print("Yes")
    else:
        print("No")

email = input("Введите email-адрес: ")
check_email(email)
def square_number(num):
    return num ** 2

x = float(input("Введите вещественное число: "))
print(square_number(x))
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

a, b, c = map(int, input("Введите три стороны треугольника через пробел: ").split())
print(is_triangle(a, b, c))
def is_long_enough(s):
    return len(s) >= 3

s = input("Введите строку: ")
print(is_long_enough(s))
def reverse_string(s):
    return s[::-1]

s = input("Введите строку: ")
print(reverse_string(s))
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))
print(sum_list(lst))
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))
print(multiply_list(lst))
def is_even(num):
    return num % 2 == 0

while True:
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
    if is_even(num):
        print(num)
def is_odd(num):
    return num % 2 != 0

lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))
odd_lst = [num for num in lst if is_odd(num)]
print(*odd_lst)
def is_odd(num):
    return num % 2 != 0

lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))
odd_lst = [num for num in lst if is_odd(num)]
print(*odd_lst)
def is_long_enough(s):
    return len(s) >= 6

cities = input("Введите список названий городов через пробел: ").split()
long_cities = [city for city in cities if is_long_enough(city)]
print(*long_cities)
def multiply_min_max(lst):
    return min(lst) * max(lst)

lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))
print(multiply_min_max(lst))
def max_of_two(a, b):
    return a if a > b else b

def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))

a, b, c = map(int, input("Введите три целых числа через пробел: ").split())
print(max_of_three(a, b, c))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Введите целое число: "))
print(is_prime(num))
def unique_elements(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst

lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))
print(unique_elements(lst))
def sort_hyphen_separated_words(s):
    words = s.split('-')
    sorted_words = sorted(words)
    return '-'.join(sorted_words)

input_string = input("Введите строку из слов, разделенных дефисами: ")
print(sort_hyphen_separated_words(input_string))
def count_case_letters(s):
    counts = {'upper': 0, 'lower': 0}
    for char in s:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
    return counts

input_string = input("Введите строку: ")
counts = count_case_letters(input_string)
print(f"Количество прописных букв: {counts['upper']}")
print(f"Количество строчных букв: {counts['lower']}")
def rectangle_operation(a, b, type=0):
    if type == 0:
        return 2 * (a + b)
    else:
        return a * b

a, b = map(int, input("Введите два числа через пробел: ").split())
type_value = int(input("Введите значение параметра type (0 или 1): "))
print(rectangle_operation(a, b, type_value))
def check_password(password, chars="$%!?@#"):
    return any(char in password for char in chars) and len(password) >= 8

password = input("Введите пароль: ")
print(check_password(password))
def enclose_in_tag(s, tag="h1"):
    return f"<{tag}>{s}</{tag}>"

input_string = input("Введите строку: ")
print(enclose_in_tag(input_string))
print(enclose_in_tag(input_string, tag="div"))
def enclose_in_tag(s, tag="h1", up=True):
    tag = tag.upper() if up else tag.lower()
    return f"<{tag}>{s}</{tag}>"

input_string = input("Введите строку: ")
print(enclose_in_tag(input_string, tag="div"))
print(enclose_in_tag(input_string, tag="div", up=False))
def filter_even_numbers(*args):
    return [num for num in args if num % 2 == 0]

numbers = map(int, input("Введите числа через пробел: ").split())
print(*filter_even_numbers(*numbers))
def longest_city_name(*cities):
    return max(cities, key=len)

cities = input("Введите названия городов через пробел: ").split()
print(longest_city_name(*cities))
lst, x, y, z = input("Введите семь целых чисел через пробел: ").split()[:4], *input().split()[4:]
print(*lst)
cities = input("Введите названия городов через пробел: ").split()
lst_c = tuple(cities)
print(lst_c)
a, b = map(int, input("Введите два целых числа a и b (a < b) через пробел: ").split())
lst = list(range(a, b + 1))
print(*lst)
numbers = input("Введите вещественные числа через пробел: ").split()
cities = input("Введите названия городов через пробел: ").split()
lst = numbers + cities
print(*lst)
abs_value = lambda x: abs(x)
num = float(input("Введите число: "))
print(abs_value(num))
add_ten = lambda x: x + 10
num = int(input("Введите число: "))
print(add_ten(num))
add_ten = lambda x: x + 10
num = int(input("Введите число: "))
print(add_ten(num))
square = lambda x: x ** 2
num = int(input("Введите число: "))
print(square(num))
divide = lambda a, b: None if b == 0 else a / b
a, b = map(int, input("Введите два целых числа через пробел: ").split())
print(divide(a, b))
contains_ra = lambda s: "ra" in s
input_string = input("Введите строку: ")
print(contains_ra(input_string))
count_occurrences = lambda s, sub: s.count(sub)
input_string = input("Введите строку: ")
substring = input("Введите подстроку: ")
print(count_occurrences(input_string, substring))
data = []
while True:
    entry = input("Введите предмет и оценку через пробел (или 0 для завершения): ")
    if entry == '0':
        break
    subject, grade = entry.split()
    data.append((subject, int(grade)))

sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
for item in sorted_data:
    print(item)
items = {}
while True:
    entry = input("Введите предмет и вес в граммах через пробел (или 0 для завершения): ")
    if entry == '0':
        break
    item, weight = entry.split()
    items[item] = int(weight)

sorted_items = sorted(items, key=items.get, reverse=True)
print(*sorted_items)
notes_order = "до ре ми фа соль ля си".split()
input_notes = input("Введите ноты через пробел: ").split()
sorted_notes = sorted(input_notes, key=lambda x: notes_order.index(x))
print(*sorted_notes)
