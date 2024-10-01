import math
# 1.1
a = int(input("1.1 Введите число:"))
print("Модуль введённого числа:", abs(a))

# 1.2
print("1.2 Введите 5 чисел через enter:")
arr_12 = [0, 0, 0, 0, 0]
for i in range (0,5):
    arr_12[i] = int(input())
print("Минимальное значение:", min(arr_12))

# 1.3
print("1.2 Введите 5 чисел через enter:")
arr_13 = [0, 0, 0, 0, 0]
for i in range (0,5):
    arr_13[i] = int(input())
print("Максимальное значение:", max(arr_13))

# 1.4
print("1.4 Введите 2 катета:")
kat1 = int(input("Первый катет = "))
kat2 = int(input("Второй катет = "))
print("Гипотенуза:", math.hypot(kat1, kat2))

# 1.5
print("1.5 Введите n и k:")
n_s = int(input("n = "))
k_s = int(input("k = "))
formula = math.factorial(n_s)/(math.factorial(k_s)*math.factorial(n_s-k_s))
print("Число сочетаний: ", formula)

# 1.6
print("1.6 Введите количество n мобилизованных и m офицеров:")
n_m = int(input("n = "))
m_o = int(input("m = "))
bus = math.ceil((n_m+m_o)/30)
print("Количество автобусов: ", bus)

# 1.7
x = int(input("1.7 Введите стоимость ручки: ")) * 0.85
st = math.floor(1000/x)
print("Количество ручек, на которые хватит денег: ", st)

# 1.8
print("1.8 Введите 3 числа через enter:")
arr_18 = [0, 0, 0]
for i in range (0,3):
    arr_18[i] = int(input())
print("В строчку: ")
print(arr_18[0], " ", arr_18[1], " ", arr_18[2])

# 1.9
print("1.9 Введите 3 числа через enter:")
arr_19 = [0, 0, 0]
for i in range (0,3):
    arr_19[i] = int(input())
print("В столбик: ")
for i in range (0,3):
    print(arr_19[i])

# 1.10 1 способ
print("1.10 1 способ: Введите 2 целых положительных числа: ")
s = int(input("Первое число = "))
d = int(input("Второе число = "))
power = math.pow(s, d)
print("Первое число в степени второго: ", power)

# 1.10 2 способ
print("1.10 2 способ: Введите 2 целых положительных числа: ")
s = int(input("Первое число = "))
d = int(input("Второе число = "))
s_d = s
for i in range (1, d):
    s_d = s_d * s
print("Первое число в степени второго: ", s_d)\

# 1.11 
print("1.11 Введите 2 вещественных числа: ")
j = float(input("Первое число = "))
h = float(input("Второе число = "))
print("Сумма чисел: ", j+h)

# 1.12
print("1.12 Количество ручек: ")
X = int(input("Синих: "))
Y = int(input("Зеленых: "))
b_p = 2 * X
r_p= 4 * Y
allpens = X + Y + b_p + r_p
print("Общее количество ручек:", allpens)

# 1.13
print("1.13 Введите длину и ширину прямоугольника: ")
w = int(input("Длина = "))
h = int(input("Ширина = "))
print("Периметр прямоугольника = ", (w+h)*2)

# 1.14
print("1.14 Pi с точностью до тысячной: ", round(math.pi, 3))

# 1.15
print("1.15 Введите стоимость и количество пирожков: ")
A = int(input("Введите стоимость пирожка в рублях: "))
B = int(input("Введите стоимость пирожка в копейках: "))
N = int(input("Введите количество пирожков: "))
total_cost_kopeks = (A * 100 + B) * N
total_rubles = total_cost_kopeks // 100
total_kopeks = total_cost_kopeks % 100
print(total_rubles, total_kopeks)

# 1.16
print("1.16 Введите вещественное число: ")
number = float(input("Введите вещественное число: "))
integer_part = int(number)
is_divisible_by_3 = integer_part % 3 == 0
print(is_divisible_by_3)

# 1.17
X = float(input("1.17 Введите стоимость покупки: "))
fractional_part = X - int(X)
is_fractional_part_greater_than_50 = fractional_part > 0.5
print(is_fractional_part_greater_than_50)


# 1.18
print("1.18 Введите стороны треугольника: ")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
is_triangle = (a + b > c) and (a + c > b) and (b + c > a)
print(is_triangle)

# 1.19
number = float(input("1.19 Введите вещественное число: "))
is_in_range = (-3 <= number <= 3) or (5 <= number <= 10)
print(is_in_range)

"""
# 1.20
print("1.20 Введите количество учащихся: ")
students_class1 = int(input("Введите количество учащихся в первом классе: "))
students_class2 = int(input("Введите количество учащихся во втором классе: "))
students_class3 = int(input("Введите количество учащихся в третьем классе: "))
desks_class1 = (students_class1 + 1) // 2
desks_class2 = (students_class2 + 1) // 2
desks_class3 = (students_class3 + 1) // 2
total_desks = desks_class1 + desks_class2 + desks_class3
print("Наименьшее число парт, которое нужно приобрести:", total_desks)

"""



