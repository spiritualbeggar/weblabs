"""
print("6.1 Введите 2 целых положительных числа: ")
n = int(input())
m = int(input())
while n <= m:
    print(n**2)
    n += 1

bookprice = float(input("6.2 Введите стоимость книги: "))
count = int(input("Введите количество книг: "))
i = 2
while i <= count:
    print(round(bookprice*i))
    i += 1

n = int(input("6.3 Введите целое положительное число "))
sum = 0
i = 1
while i <= n:
    sum += 1 / i
    i += 1
print(f"{sum:.3f}")

print("6.4 Вводите числа:")
sum = 0
while True:
    num = int(input())
    if num == 0:
        break
    sum += num
print("Сумма введенных чисел: ", sum)

print("6.5 Введите строку с подряд идущими дефисами: ")
s = input()
while '--' in s:
    s = s.replace('--', '-')
print(s)

n = int(input("6.6 Введите целое положительное число (трёхзначное и выше): "))
product = 1
while n > 0:
    product *= n % 10
    n //= 10
print(product)

n = int(input("6.7 Введите длину последовательности Фибоначчи: "))
a, b = 1, 1
result = []
while n > 0:
    result.append(a)
    a, b = b, a + b
    n -= 1
print(' '.join(map(str, result)))

n = int(input("6.8 Введите количество часов: "))
cells = 1
hours = 0
while hours < n:
    if hours % 3 == 0 and hours != 0:
        cells *= 2
    hours += 1
print("Количество клеток: ", cells)

n = int(input("6.9 Введите количество лет: "))
deposit = 1000
years = 0
while years < n:
    deposit += deposit * 0.05
    years += 1
print(f"{deposit:.2f}")

print("6.10 Введите два натуральных четных числа в строку через пробел:")
n, m = map(int, input().split())
n += 1
result = []
while n < m:
    result.append(n)
    n += 2
print(' '.join(map(str, result)))

print("6.11")
num = 100
result = []
while num < 1000:
    if num % 47 == 43 and num % 3 == 0:
        result.append(num)
    num += 1
print(' '.join(map(str, result)))

print("6.12")
lst = [0] * 10
count = 0
while count < 5:
    p = int(input())
    if lst[p] == 1:
        continue
    lst[p] = 1
    count += 1
print(' '.join(map(str, lst)))

print("6.13 Введите числа:")
product = 1
while True:
    num = int(input())
    if num == 0:
        break
    if num < 0:
        continue
    product *= num
print(product)

print("6.14 Введите список названий городов в одну строчку через пробел: ")
cities = input().split()
i = 0
while i < len(cities):
    if len(cities[i]) <= 5:
        print("No")
        break
    i += 1
else:
    print("Yes")
    

print("6.15 Введите имена студентов в одну строку через пробел: ")
names = input().split()
i = 0
while i < len(names):
    name = names[i].lower()
    if name[0] == name[-1]:
        print("Yes")
        break
    i += 1
else:
    print("No")


n = int(input("6.16 Введите натуральное положительное число: "))
if n >= 100:
    print("Слишком большое значение n")
else:
    result = []
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
        i += 1
    print(' '.join(map(str, result)))

n = int(input("6.17 Введите натуральное положительное число: "))
i = 1
while i * i <= n:
    i += 1
print(i)

x = int(input("6.18 Введите километры: "))
distance = 10
day = 1
while distance <= x:
    distance += distance * 0.1
    day += 1
print(day)

print("6.19 Введите названия книг с новой строки: ")
books = []
while True:
    book = input()
    if book == "":
        break
    books.append(book)
result = []
i = 0
while i < len(books):
    if ' ' not in books[i]:
        result.append(books[i])
    i += 1
print(' '.join(result))

print("6.20")
print(' '.join(map(str, range(11))))

print("6.21")
print(' '.join(map(str, range(10, -1, -1))))

print("6.22")
print(' '.join(map(str, range(-10, 0, 2))))

print("6.23")
print(' '.join(map(str, range(1, 20, 3))))

print("6.24 Введите целые числа в строчку через пробел: ")
numbers = list(map(int, input().split()))
sum_odd = 0
for num in numbers:
    if num % 2 != 0:
        sum_odd += num
print(sum_odd)

cities = input("6.25 Введите города в строчку через пробел: ").split()
lengths = []
for city in cities:
    lengths.append(len(city))
print(' '.join(map(str, lengths)))

n = int(input("6.26 Введите натуральное число: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')

n = int(input("6.27 Введите натуральное число: "))
is_prime = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print("ДА" if is_prime and n > 1 else "НЕТ")
cities = input("6.28 Введите список городов в одну строчку через пробел: ").split()
valid = True
for i in range(len(cities) - 1):
    last_char = cities[i][-1]
    if last_char in 'ьъы':
        last_char = cities[i][-2]
    if cities[i + 1][0].lower() != last_char.lower():
        valid = False
        break
print("ДА" if valid else "НЕТ")

n = int(input("6.29 Введите натуральное число: "))
sum_multiples = 0
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        sum_multiples += i
print(sum_multiples)
s = input("6.30 Введите строку: ")
indices = []
for i in range(len(s) - 1):
    if s[i:i+2] == 'ра':
        indices.append(i)
if indices:
    print(' '.join(map(str, indices)))
else:
    print(-1)


phone = input("6.31 Введите номер телефона: ")
if len(phone) == 16 and phone[0] == '+' and phone[1] == '7' and phone[2] == '(' and phone[6] == ')' and phone[10] == '-' and phone[13] == '-':
    valid = True
    for i in range(3, 6):
        if not phone[i].isdigit():
            valid = False
            break
    for i in range(7, 10):
        if not phone[i].isdigit():
            valid = False
            break
    for i in range(11, 13):
        if not phone[i].isdigit():
            valid = False
            break
    for i in range(14, 16):
        if not phone[i].isdigit():
            valid = False
            break
    print("Yes" if valid else "No")
else:
    print("No")


expression = input("6.32 Введите выражение: ").replace(' ', '')
result = 0
current_number = ''
current_operator = '+'
for char in expression:
    if char.isdigit():
        current_number += char
    else:
        result = eval(f"{result}{current_operator}{current_number}")
        current_number = ''
        current_operator = char
result = eval(f"{result}{current_operator}{current_number}")
print(result)

numbers = list(map(int, input("6.33 Введите целые числа в строку через пробел: ").split()))
for i, num in enumerate(numbers):
    numbers[i] = num ** 2
print(' '.join(map(str, numbers)))

numbers = input("6.34  Введите целые числа в строку через пробел: ").split()
duplicated = []
for num in numbers:
    duplicated.append(num)
    duplicated.append(num)
print(' '.join(duplicated))

numbers = list(map(float, input("6.35  Введите вещественные числа в одну строку через пробел: ").split()))
min_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
print(min_value)

numbers = list(map(float, input("6.36  Введите вещественные числа в одну строку через пробел: ").split()))
for i, num in enumerate(numbers):
    if num < 0:
        numbers[i] = -1.0
print(' '.join(map(str, numbers)))

cities = iter(input("6.37  Введите список городов в одну строчку через пробел: ").split())
print(next(cities))
print(next(cities))

print("6.38")
s = input("Введите строку: ")
it = iter(s)
while True:
    char = next(it)
    if char == ' ':
        break
    print(char, end='')

print("6.39")
num = input("Введите четырехзначное целое положительное число: ")
it = iter(num)
print(next(it), next(it), next(it), next(it))

print("6.40 Введите натуральное число: ")
N = int(input())
matrix = [[1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    matrix[i][-1] = 5
for row in matrix:
    print(' '.join(map(str, row)))

print("6.41 Введите список URL: ")
input_lines = input().strip().split('\n')
for url in input_lines:
    print('-'.join(url.split()))

n = int(input("6.42 Введите натуральное число: "))
is_prime = [True] * n
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, n, i):
            is_prime[j] = False
primes = [i for i in range(2, n) if is_prime[i]]
print(' '.join(map(str, primes)))

print("6.43 Введите двумерный список 5х5: ")
matrix = [list(map(int, input().split())) for _ in range(5)]
def check_surroundings(i, j):
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if 0 <= x < 5 and 0 <= y < 5 and (x != i or y != j):
                if matrix[x][y] == 1:
                    return False
    return True
valid = True
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            if not check_surroundings(i, j):
                valid = False
                break
    if not valid:
        break

print("Yes" if valid else "No")

print("6.44 Введите двумерный список 5х5: ")
matrix = [list(map(int, input().split())) for _ in range(5)]
def is_symmetric():
    for i in range(5):
        for j in range(5):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

print("Yes" if is_symmetric() else "No")

n = int(input("6.45 Введите натуральное число: "))
denominations = [64, 32, 16, 8, 4, 2, 1]
result = []
for denom in denominations:
    while n >= denom:
        result.append(denom)
        n -= denom
print(" ".join(map(str, result)))

print("6.46 Введите вещественные чичсла в строку через пробел: ")
numbers = list(map(float, input().split()))
result = [abs(num) for num in numbers]
print(result)

number = input("6.47 Введите целое семизначное положительное число: ")
result = [int(digit) for digit in number]
print(result)

print("6.48 Введите названия городов в строку через пробел: ")
cities = input().split()
result = [city for city in cities if len(city) > 5]
print(" ".join(result))

n = int(input("6.49 Введите натуральное число: "))
divisors = [i for i in range(1, n + 1) if n % i == 0]
print(" ".join(map(str, divisors)))

N = int(input("6.50 Введите натуральное число: "))
matrix = [[i] * N for i in range(N)]
for row in matrix:
    print(" ".join(map(str, row)))

print("6.51 Введите список вещественных чисел: ")
numbers = list(map(float, input().split()))
result = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
print(" ".join(map(str, result)))

print("6.52 Введите два списка целых чисел одинаковой длины: ")
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
result = [list1[i] + list2[i] for i in range(len(list1))]
print(" ".join(map(str, result)))

print("6.53 Введите список: ")
data = input().split()
result = [[data[i], int(data[i+1])] for i in range(0, len(data), 2)]
print(result)
"""
print("6.54 Введите ваш пароль: ")
password = input()
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "$#@!%?^&" for c in password)
is_long_enough = len(password) >= 6
if has_lower and has_upper and has_digit and has_special and is_long_enough:
    print("Yes")
else:
    print("No")