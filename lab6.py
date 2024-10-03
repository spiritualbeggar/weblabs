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
"""
n = int(input("6.6 Введите целое положительное число (трёхзначное и выше): "))
product = 1
while n > 0:
    product *= n % 10
    n //= 10
print(product)