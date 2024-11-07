print("2.1. Введите название и возраст животного: ")
class Animal:
    def __init__(self,name,old):
        self.name=name
        self.old=old
class Cat(Animal):
    def __init__(self,name,old,color,weight):
        super().__init__(name,old)
        self.color=color
        self.weight=weight
    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"
class Dog(Animal):
    def __init__(self,name,old,breed,size):
        super().__init__(name,old)
        self.breed=breed
        self.size=size
    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"
name=input("Введите название животного: ")
old=int(input("Введите возраст животного: "))
color=input("Введите цвет кошки: ")
weight=float(input("Введите вес кошки: "))
cat=Cat(name,old,color,weight)
print(cat.get_info())
breed=input("Введите породу собаки: ")
size=(float(input("Введите высоту собаки: ")),float(input("Введите длину собаки: ")))
dog=Dog(name,old,breed,size)
print(dog.get_info())

print("2.2. Введите данные для физического и электронного товара: ")
class Thing:
    _id=0
    def __init__(self,name,price):
        self.id=Thing._id
        Thing._id+=1
        self.name=name
        self.price=price
        self.weight=None
        self.dims=None
        self.memory=None
        self.frm=None
    def get_data(self):
        return (self.id,self.name,self.price,self.weight,self.dims,self.memory,self.frm)
class Table(Thing):
    def __init__(self,name,price,weight,dims):
        super().__init__(name,price)
        self.weight=weight
        self.dims=dims
class ElBook(Thing):
    def __init__(self,name,price,memory,frm):
        super().__init__(name,price)
        self.memory=memory
        self.frm=frm
name=input("Введите название товара: ")
price=float(input("Введите цену товара: "))
weight=float(input("Введите вес стола: "))
dims=(float(input("Введите длину стола: ")),float(input("Введите ширину стола: ")),float(input("Введите глубину стола: ")))
table=Table(name,price,weight,dims)
print(*table.get_data())
memory=int(input("Введите объем памяти электронной книги: "))
frm=input("Введите формат электронной книги: ")
book=ElBook(name,price,memory,frm)
print(*book.get_data())

print("2.3. Введите список целых чисел: ")
class ListInteger(list):
    def __init__(self,iterable):
        for value in iterable:
            self._check_integer(value)
        super().__init__(iterable)
    def __setitem__(self,index,value):
        self._check_integer(value)
        super().__setitem__(index,value)
    def append(self,value):
        self._check_integer(value)
        super().append(value)
    def _check_integer(self,value):
        if not isinstance(value,int):
            raise TypeError('Можно передавать только целочисленные значения')
s=ListInteger(map(int,input("Введите целые числа через пробел: ").split()))
index,value=map(int,input("Введите индекс и значение для изменения элемента: ").split())
s[index]=value
s.append(int(input("Введите значение для добавления в список: ")))
print(s)

print("2.4. Введите итерируемые объекты для сложения: ")
class Tuple(tuple):
    def __add__(self,other):
        return Tuple(super().__add__(tuple(other)))
t=Tuple(map(int,input("Введите начальный кортеж (через пробел): ").split()))
iter_obj1=input("Введите первый итерируемый объект: ")
t=t+iter_obj1
print(t)
iter_obj2=input("Введите второй итерируемый объект: ")
t=t+iter_obj2
print(t)

print("2.5. Введите строку для создания SoftList: ")
class SoftList(list):
    def __getitem__(self,index):
        if index>=len(self) or index<-len(self):
            return False
        return super().__getitem__(index)
sl=SoftList(input("Введите строку: "))
index=int(input("Введите индекс для получения элемента: "))
print(sl[index])

print("2.6. Введите данные для книги и цифровой книги: ")
class Book:
    def __init__(self,title,author,pages,year):
        self.title=title
        self.author=author
        self.pages=pages
        self.year=year
class DigitBook(Book):
    def __init__(self,title,author,pages,year,size,frm):
        super().__init__(title,author,pages,year)
        self.size=size
        self.frm=frm
title=input("Введите название книги: ")
author=input("Введите автора книги: ")
pages=int(input("Введите число страниц: "))
year=int(input("Введите год издания: "))
book1=Book(title,author,pages,year)
size=int(input("Введите размер цифровой книги в байтах: "))
frm=input("Введите формат цифровой книги: ")
book2=DigitBook(title,author,pages,year,size,frm)
data=lambda obj:[print(f'{key:6} --> {value}') for key,value in obj.__dict__.items()]
data(book1)
print('*'*25)
data(book2)

print("2.7. Введите параметры для добавления объектов недвижимости: ")
class SellItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class House(SellItem):
    def __init__(self,name,price,material,square):
        super().__init__(name,price)
        self.material=material
        self.square=square
class Flat(SellItem):
    def __init__(self,name,price,size,rooms):
        super().__init__(name,price)
        self.size=size
        self.rooms=rooms
class Land(SellItem):
    def __init__(self,name,price,square):
        super().__init__(name,price)
        self.square=square
class Agency:
    def __init__(self,name):
        self.name=name
        self._objects=[]
    def add_object(self,obj):
        if isinstance(obj,SellItem):
            self._objects.append(obj)
    def remove_object(self,obj):
        if obj in self._objects:
            self._objects.remove(obj)
    def get_objects(self):
        return self._objects
agency_name=input("Введите название агентства: ")
ag=Agency(agency_name)
for _ in range(3):
    obj_type=input("Введите тип объекта (Flat, House, Land): ")
    name=input("Введите название объекта: ")
    price=float(input("Введите цену объекта: "))
    if obj_type=="Flat":
        size=float(input("Введите размер квартиры: "))
        rooms=int(input("Введите число комнат: "))
        ag.add_object(Flat(name,price,size,rooms))
    elif obj_type=="House":
        material=input("Введите материал дома: ")
        square=float(input("Введите площадь дома: "))
        ag.add_object(House(name,price,material,square))
    elif obj_type=="Land":
        square=float(input("Введите площадь земельного участка: "))
        ag.add_object(Land(name,price,square))
for obj in ag.get_objects():
    print(obj.name)

print("2.8. Введите данные для продуктов питания: ")
class Food:
    def __init__(self,name,weight,calories):
        self._name=name
        self._weight=weight
        self._calories=calories
    def get_data(self):
        return self._name
class BreadFood(Food):
    def __init__(self,name,weight,calories,white):
        super().__init__(name,weight,calories)
        self._white=white
class SoupFood(Food):
    def __init__(self,name,weight,calories,dietary):
        super().__init__(name,weight,calories)
        self._dietary=dietary
class FishFood(Food):
    def __init__(self,name,weight,calories,fish):
        super().__init__(name,weight,calories)
        self._fish=fish
for _ in range(3):
    food_type=input("Введите тип еды (BreadFood, SoupFood, FishFood): ")
    name=input("Введите название продукта: ")
    weight=float(input("Введите вес продукта: "))
    calories=int(input("Введите калорийность продукта: "))
    if food_type=="BreadFood":
        white=bool(int(input("Белый хлеб? (1-да, 0-нет): ")))
        food=BreadFood(name,weight,calories,white)
    elif food_type=="SoupFood":
        dietary=bool(int(input("Диетический суп? (1-да, 0-нет): ")))
        food=SoupFood(name,weight,calories,dietary)
    elif food_type=="FishFood":
        fish=input("Введите тип рыбы: ")
        food=FishFood(name,weight,calories,fish)
    print(food.get_data())

print("2.9. Введите числовой массив и индекс: ")
class Array:
    def __init__(self,*args):
        self.__data=list(args)
    def __getitem__(self,index):
        if index>=len(self.__data):
            raise IndexError('неверный индекс')
        return self.__data[index]
    def __setitem__(self,index,value):
        if index>=len(self.__data):
            raise IndexError('неверный индекс')
        self.__data[index]=value
    def __str__(self):
        return " ".join(map(str,self.__data))
a=Array(*map(int,input("Введите массив чисел через пробел: ").split()))
print("Текущий массив:",a)
index,value=map(int,input("Введите индекс и значение для изменения элемента: ").split())
a[index]=value
print("Измененный массив:",a)

