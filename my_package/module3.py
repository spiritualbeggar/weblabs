from random import seed, random as rnd

def my_rnd():
    seed(10)
    return round(rnd(), 2)