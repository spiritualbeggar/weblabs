def print_area_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        return result
    return wrapper

@print_area_decorator
def rectangle_area(width, height):
    return width * height

width, height = map(int, input("Введите ширину и высоту прямоугольника через пробел: ").split())
rectangle_area(width, height)
def sort_list_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return sorted(result)
    return wrapper

@sort_list_decorator
def string_to_list(s):
    return list(map(int, s.split()))

input_string = input("Введите строку из целых чисел через пробел: ")
lst = string_to_list(input_string)
print(*lst)
def list_to_dict_decorator(func):
    def wrapper(*args, **kwargs):
        list1, list2 = func(*args, **kwargs)
        return dict(zip(list1, list2))
    return wrapper

@list_to_dict_decorator
def string_to_lists(s1, s2):
    return s1.split(), s2.split()

input_string1 = input("Введите первую строку из слов через пробел: ")
input_string2 = input("Введите вторую строку из слов через пробел: ")
d = string_to_lists(input_string1, input_string2)
print(*sorted(d.items()))
from functools import wraps

def bold_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

def underline_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper

@bold_decorator
@italic_decorator
@underline_decorator
def return_string(s):
    return s

input_string = input("Введите строку текста: ")
print(return_string(input_string))
a, b = map(int, input("Введите два целых числа a и b (a < b) через пробел: ").split())
generator = (x**2 for x in range(a, b + 1))
result = tuple(generator)
print(*result)
a, b = map(int, input("Введите два целых числа a и b (a < b) через пробел: ").split())
generator = (abs(x) for x in range(a, b + 1))
print(*generator)
a, b = map(int, input("Введите два целых числа a и b (a < b) через пробел: ").split())
generator1 = (abs(x) for x in range(a, b + 1))
generator2 = (x**3 for x in generator1)
print(*generator2)
from string import ascii_lowercase

combinations = (f"{c1}{c2}" for c1 in ascii_lowercase for c2 in ascii_lowercase)
result = [next(combinations) for _ in range(30)][20:30]
print(*result)
def sum_generator(n):
    current_sum = 0
    for i in range(1, n + 1):
        current_sum += i
        yield current_sum

n = int(input("Введите натуральное число n: "))
print(*sum_generator(n))
numbers = list(map(int, input("Введите строку из целых чисел через пробел: ").split()))
filtered_numbers = filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers)
print(*filtered_numbers)
numbers = list(map(int, input("Введите строку из целых чисел через пробел: ").split()))
even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
odd_count = len(list(filter(lambda x: x % 2 != 0, numbers)))
print(f"Количество четных чисел: {even_count}")
print(f"Количество нечетных чисел: {odd_count}")
numbers = list(map(int, input("Введите строку из целых чисел через пробел: ").split()))
palindromes = filter(lambda x: str(x) == str(x)[::-1], numbers)
print(*palindromes)
words = input("Введите строку из слов, разделенных пробелами: ").split()
six_letter_words = filter(lambda x: len(x) == 6, words)
print(*six_letter_words)
numbers = list(map(int, input("Введите строку из целых чисел через пробел: ").split()))
tripled_numbers = map(lambda x: x * 3, numbers)
print(*tripled_numbers)
list1 = list(map(int, input("Введите первую строку из целых чисел через пробел: ").split()))
list2 = list(map(int, input("Введите вторую строку из целых чисел через пробел: ").split()))
list3 = list(map(int, input("Введите третью строку из целых чисел через пробел: ").split()))
summed_lists = map(lambda x, y, z: x + y + z, list1, list2, list3)
print(*summed_lists)
data = []
while True:
    entry = input("Введите имя, фамилию, дату рождения и вес через решетку # (или 0 для завершения): ")
    if entry == '0':
        break
    data.append(entry.split('#'))

names_and_surnames = map(lambda x: x[0].strip(), data)
birth_dates = map(lambda x: x[1].strip(), data)
weights = map(lambda x: x[2].strip().rstrip('kg'), data)

print("Как зовут:", ', '.join(names_and_surnames))
print("Родился:", ', '.join(birth_dates))
print("Весит:", ', '.join(weights))
numbers = input("Введите строку из вещественных чисел через пробел: ").split()
float_numbers = map(float, numbers)
print(*[next(float_numbers) for _ in range(3)])
list1 = map(int, input("Введите первый список целых чисел через пробел: ").split())
list2 = map(int, input("Введите второй список целых чисел через пробел: ").split())
multiplied_pairs = map(lambda x, y: x * y, list1, list2)
print(*[next(multiplied_pairs) for _ in range(3)])
words = input("Введите строку из слов, записанных через пробел: ").split()
rows = [words[i:i+3] for i in range(0, len(words), 3)]
for row in rows:
    print(*row)