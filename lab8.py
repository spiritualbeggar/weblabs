print("Задание 8.1. Введите вещественные числа через пробел:")
s=set(map(float,input().split()))
print(*sorted(s))

print("Задание 8.2. Введите текст:")
print(len(set(input().lower().split())))

print("Задание 8.3. Введите строку:")
digits=sorted(set(filter(str.isdigit,input())))
print(" ".join(digits) if digits else "No")

print("Задание 8.4. Введите список гостей (завершите ввод числом 0):")
s=set()
while True:
    name=input()
    if name=='0':break
    s.add(name)
print(len(s))

print("Задание 8.5. Введите список комментариев (завершите ввод числом 0):")
s=set()
while True:
    comment=input()
    if comment=='0':break
    s.add(comment.split(':')[0])
print(len(s))

print("Задание 8.6. Введите названия городов (завершите ввод числом 0):")
s=set()
while True:
    city=input()
    if city=='0':break
    s.add(city)
print(len(s))

print("Задание 8.7. Введите два списка целых чисел через пробел:")
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
print(*sorted(s1&s2))

print("Задание 8.8. Введите два списка целых чисел через пробел:")
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
print(*sorted(s1-s2))

print("Задание 8.9. Введите два списка целых чисел через пробел:")
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
print(*sorted(s1^s2))

print("Задание 8.10. Введите два списка городов через пробел:")
s1=set(input().split())
s2=set(input().split())
print("Yes" if s1==s2 else "No")

print("Задание 8.11. Введите список оценок через пробел:")
s=set(map(int,input().split()))
print("ДОПУЩЕН" if 2 not in s else "НЕ ДОПУЩЕН")

print("Задание 8.12. Введите два списка городов через пробел:")
s1=set(input().split())
s2=set(input().split())
print("Yes" if s1<=s2 else "No")

print("Задание 8.13. Введите натуральное число:")
n=int(input())
factors={2,3,5}
s=set()
for p in [2,3,5,7,11,13]:
    while n%p==0:
        s.add(p)
        n//=p
print("Yes" if factors<=s else "No")