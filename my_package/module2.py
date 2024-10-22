from random import seed, randint

def my_randint(a, b):
    seed(1)
    return randint(a, b)