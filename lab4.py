print("4.1 Введите целые числа через пробел:")
t=(5.45,-18.9)+tuple(map(int,input().split()))
print(t)

print("4.2 Введите названия городов через пробел:")
cities=tuple(input().split())
cities+=(('Москва',)*(not 'Москва' in cities))
print(*cities)

print("4.3 Введите названия городов через пробел:")
cities=tuple(input().split())
new_cities=cities[:-2]+cities[-1:]
print(*new_cities)

print("4.4 Введите имена студентов через пробел:")
students=tuple(input().split())
print("Введите искомое имя:")
name=input()
print(students.count(name))

print("4.5 Введите оценки студента через пробел:")
grades=tuple(map(int,input().split()))
avg=sum(grades)/len(grades)
print(f"{avg:.1f}")

print("4.6 Введите названия городов через пробел:")
cities=tuple(input().split())
print("Введите название одного города:")
start_city=input()
start_index=cities.index(start_city)
print(cities[start_index::2])

print("4.7 Введите оценки студента через пробел:")
grades=tuple(map(int,input().split()))
print(grades[2:7][::-1])

print("4.8 Введите три набора целых чисел через пробел:")
t1=tuple(map(int,input().split()))
t2=tuple(map(int,input().split()))
t3=tuple(map(int,input().split()))
t=(t1,t2,t3)
print(sum(t[i][-1] for i in range(3)))

print("4.9 Введите три числа с плавающей точкой через пробел:")
l,w,h=map(float,input().split())
v=l*w*h
print(f"{v:_.2f}".replace('.',',').replace('_','_'))

print("4.10 Введите три набора целых чисел через пробел:")
t1=tuple(map(int,input().split()))
t2=tuple(map(int,input().split()))
t3=tuple(map(int,input().split()))
t=(t1,t2,t3)
avg=[sum(t[i])/len(t[i]) for i in range(3)]
print(*[f"{x:.1f}" for x in avg])