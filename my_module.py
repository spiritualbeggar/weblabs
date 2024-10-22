from math import ceil, floor
from random import seed, randint, random as rnd

def my_ceil(number):
    return ceil(number)

def my_floor(number):
    return floor(number)

def my_randint(a, b):
    seed(1)
    return randint(a, b)

def my_rnd():
    seed(10)
    return round(rnd(), 2)
