print(11.1)
import math
number = float(input("Введите вещественное число: "))
print(math.ceil(number))

print(11.2)
from math import floor
number = float(input("Введите вещественное число: "))
print(floor(number))

print(11.3)
from random import seed, randint
a, b = map(int, input("Введите два целых числа a и b (a < b), разделенных пробелом: ").split())
seed(1)
print(randint(a, b))

print(11.4)
from random import seed, random as rnd
seed(10)
print(round(rnd(), 2))

from my_module import my_ceil, my_floor, my_randint, my_rnd
number = float(input("Введите вещественное число: "))
print(my_ceil(number))
print(my_floor(number))
a, b = map(int, input("Введите два целых числа a и b (a < b), разделенных пробелом: ").split())
print(my_randint(a, b))
print(my_rnd())

print(11.6)
from my_package.module1 import my_ceil, my_floor
from my_package.module2 import my_randint
from my_package.module3 import my_rnd
number = float(input("Введите вещественное число: "))
print(my_ceil(number))
print(my_floor(number))
a, b = map(int, input("Введите два целых числа a и b (a < b), разделенных пробелом: ").split())
print(my_randint(a, b))
print(my_rnd())