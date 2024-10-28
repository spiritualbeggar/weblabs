# Задание 1.1
class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Том Круз"
    views = 153
    comments = 15

# Задание 1.2
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024
Goods.price = 2048
Goods.inflation = 100

# Задание 1.3
class Car:
    pass
setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Белый")
setattr(Car, 'number', "Е777КХ37")
print(Car.__dict__['color'])

# Задание 1.4
class Notes:
    uid = 100837
    title = "Ave Maria"
    author = "И.С. Бах"
    pages = 5
print(getattr(Notes, 'author'))

# Задание 1.5
class Dictionary:
    rus = "Питон"
    eng = "Python"
print(getattr(Dictionary, 'rus_word', False))

# Задание 1.6
class TravelBlog:
    total_blogs = 0
tb1 = TravelBlog()
tb1.name = 'Франция'
tb1.days = 6
TravelBlog.total_blogs += 1
tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5
TravelBlog.total_blogs += 1
print(TravelBlog.total_blogs, tb2.total_blogs)

# Задание 1.7
class Figure:
    type_fig = 'ellipse'
    color = 'red'
fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
del fig1.color
print(' '.join(fig1.__dict__.keys()), Figure.color)

# Задание 1.8
class Person:
    name = 'Юрий Тверской'
    job = 'Писатель'
    city = 'Иваново'
person = Person()
print(hasattr(person, 'job'))

# Задание 1.9
class MediaPlayer:
    def open(self, file):
        self.filename = file
    def play(self):
        print(f"Воспроизведение {self.filename}")
media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open("filemedia1")
media2.open("filemedia2")
media1.play()
media2.play()

# Задание 1.10
class Graph:
    LIMIT_Y = [0, 10]
    def set_data(self, data):
        self.data = data
    def draw(self):
        result = [str(num) for num in self.data if num in range(self.LIMIT_Y[0], self.LIMIT_Y[1] + 1)]
        print(" ".join(result))
graph_1 = Graph()
data = list(map(int, input("1.10. Введите данные через пробел: ").split()))
graph_1.set_data(data)
graph_1.draw()

# Задание 1.11
class Translator:
    def __init__(self):
        self.dict = {}
    def add(self, eng, rus):
        if eng not in self.dict:
            self.dict[eng] = []
        if rus not in self.dict[eng]:
            self.dict[eng].append(rus)
    def remove(self, eng):
        if eng in self.dict:
            del self.dict[eng]
    def translate(self, eng):
        return self.dict.get(eng, [])
tr = Translator()
while True:
    entry = input("1.11. Введите слово (или 0 для завершения): ")
    if entry == "0":
        break
    eng, rus = entry.split(" - ")
    tr.add(eng, rus)
word_to_translate = input("Введите слово для перевода: ")
print(" ".join(tr.translate(word_to_translate)))

# Задание 1.12
class Money:
    def __init__(self, amount):
        self.money = amount
my_money = Money(100)
your_money = Money(1000)

# Задание 1.13
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color
points = [Point(i, i) for i in range(1, 2001, 2)]
points[1].color = 'yellow'

# Задание 1.14
import random
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
elements = [random.choice([Line, Rect, Ellipse])(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)) for _ in range(217)]
for element in elements:
    if isinstance(element, Line):
        element.sp = (0, 0)
        element.ep = (0, 0)

# Задание 1.15
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if not all(isinstance(x, (int, float)) and x > 0 for x in (self.a, self.b, self.c)):
            return 1
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 2
        return 3
a, b, c = map(float, input("1.15. Введите три длины сторон треугольника через пробел: ").split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

# Задание 1.16
class AbstractClass:
    def __new__(cls):
        return "Ошибка: нельзя создавать объекты абстрактного класса"
obj = AbstractClass()
print(obj)

# Задание 1.17
class SingletonFive:
    instances = []
    def __new__(cls, name):
        if len(cls.instances) < 5:
            instance = super(SingletonFive, cls).__new__(cls)
            cls.instances.append(instance)
            instance.name = name
            return instance
        return cls.instances[-1]
objs = [SingletonFive(str(n)) for n in range(10)]
print(objs[4], objs[5], objs[6], objs[7])

# Задание 1.18
TYPE_OS = 1
class DialogWindows:
    name_class = "DialogWindows"
class DialogLinux:
    name_class = "DialogLinux"
class Dialog:
    def __new__(cls, name):
        if TYPE_OS == 1:
            return DialogWindows()
        return DialogLinux()
dlg = Dialog("Dialog")
print(dlg)

# Задание 1.19
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def clone(self):
        return Point(self.x, self.y)
pt = Point(5, 10)
pt_clone = pt.clone()
print(pt, vars(pt))
print(pt_clone, vars(pt_clone))

# Задание 1.20
class Factory:
    @staticmethod
    def build_sequence():
        return []
    @staticmethod
    def build_number(string):
        return int(string)
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
print(res)

# Задание 1.21
class Clock:
    def __init__(self):
        self.__
