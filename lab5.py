"""
print("5.1 Введите 2 вещественных числа: ")
input_line=input()
numbers=input_line.split()
num1=float(numbers[0])
num2=float(numbers[1])
if num1>num2:print(num1)
else:print(num2)

print("5.2 Введите слово: ")
word=input().lower()
if word==word[::-1]:print("Palindrome")
else:print("Not a Palindrome")

print("5.3 Введите два целых положительных числа: ")
a,b=map(int,input().split())
if a%b==0:print(a//b)
else:print(f"{a} на {b} нацело не делится")

print("5.4 Введите три целых положительных числа: ")
a,b,c=map(int,input().split())
if a**2+b**2==c**2:print("Yes")
else:print("No")

print("5.6 Введите пятизначное число: ")
n=input()
if n[-1]=='7':print("Yes")
else:print("No")

print("5.6 Введите слово: ")
word=input().lower()
if 't' in word and 'h' in word and 'o' in word:print("Yes")
else:print("No")

print("5.7 Введите список городов: ")
cities=input().split()
if 'Москва' in cities:cities.remove('Москва')
print(' '.join(cities))

print("5.8 Введите четыре целых числа: ")
a,b,c,d=map(int,input().split())
if (c+2<=a and d+2<=b) or (c+2<=b and d+2<=a):print("Yes")
else:print("No")

print("5.9 Введите шестизначное число: ")
n=input()
if int(n[0])+int(n[1])+int(n[2])==int(n[3])+int(n[4])+int(n[5]):print("Yes")
else:print("No")

print("5.10 Введите вещественное число: ")
t=float(input())
if int(t)%5<3:print("green")
else:print("red")

print("5.11 Введите число от 1 до 6: ")
n=int(input())
if n==1:print("1. Введение в Python")
elif n==2:print("2. Строки и списки")
elif n==3:print("3. Условные операторы")
elif n==4:print("4. Циклы")
elif n==5:print("5. Словари, кортежи и множества")
elif n==6:print("6. Выход")

print("5.12 Введите три целых числа через пробел: ")
a,b,c=map(int,input().split())
if a<=b and a<=c:print(a)
elif b<=a and b<=c:print(b)
else:print(c)

print("5.13 Введите вес боксера: ")
w=float(input())
if w<=60:print(1)
elif w<=64:print(2)
elif w<=69:print(3)
else:print(4)

print("5.14 Введите порядковый номер дня недели: ")
n=int(input())
if n==1:print("понедельник")
elif n==2:print("вторник")
elif n==3:print("среда")
elif n==4:print("четверг")
elif n==5:print("пятница")
elif n==6:print("суббота")
elif n==7:print("воскресенье")

print("5.15 Введите порядковый номер месяца: ")
m=int(input())
if m in [1,3,5,7,8,10,12]:print(31)
elif m in [4,6,9,11]:print(30)
else:print(28)

print("5.16 Введите число и месяц: ")
d,m=map(int,input().split())
days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
prev_d=d-1
prev_m=m
if prev_d==0:
    prev_m-=1
    prev_d=days_in_month[prev_m-1]
next_d=d+1
next_m=m
if next_d>days_in_month[m-1]:
    next_m+=1
    next_d=1
print(f"{prev_d:02d}.{prev_m:02d} {next_d:02d}.{next_m:02d}")

print("5.17 Введите k (1<= k <= 365): ")
k=int(input())
days=["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"]
print(days[(k-1)%7])

print("5.18 Введите два вещественных числа: ")
a=float(input())
b=float(input())
max_val=a if a>b else b
print(max_val)

print("5.19 Введите целое число: ")
n=int(input())
result="a multiple of 5" if n%5==0 else "not a multiple of 5"
print(f"{n} is {result}")

print("5.20 Введите слово: ")
word=input().lower()
result="Palindrome" if word==word[::-1] else "Not a Palindrome"
print(result)

print("5.21 Введите целое число 0 или 1: ")
n=int(input())
result=True if n==1 else False
print(result)

print("5.22 Введите текущее время (секунды) в диапазоне [0;59]: ")
t=int(input())
next_t=0 if t==59 else t+1
print(next_t)

print("5.23 Введите температуру в Цельсиях или Фаренгейтах: ")
t=int(input())
scale=input().upper()
result=int(t*1.8+32) if scale=='C' else int((t-32)/1.8) if scale=='F' else "Неправильно введены градусы"
print(result)

print("5.24 Введите букву: ")
letter=input().lower()
vowels_ru="аоуиыэеёюя"
vowels_en="aeiou"
if letter in vowels_ru or letter in vowels_en:print("Гласная")
elif letter in "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz":print("Согласная")
elif letter in "ъь":print(letter)
else:print("Неправильно введена буква")
"""
print("5.25 Введите размер собаки и возраст в годах: ")
size = input().upper()
age = int(input())

if size == 'М':
    human_age = 16 * age + 31 if age > 2 else 10.5 * age
elif size == 'С':
    human_age = 12 * age + 31 if age > 2 else 10.5 * age
elif size == 'К':
    human_age = 8 * age + 31 if age > 2 else 10.5 * age
else:
    human_age = "Неправильно введен размер"
print(human_age)







