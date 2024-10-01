"""
print("2.1")
hi = input("Введите первую фразу: ")
ily = input("Введите первую фразу: ")
print(hi + " " + ily)

print("2.2")
phase1 = input("Введите первую фразу: ")
phase2 = input("Введите первую фразу: ")
print(str(phase1*2) + " " +  str(phase2*3))

print("2.3")
a = int(input("Переменная a = "))
b = int(input("Переменная b = "))
print("Переменная a = " + str(a), ", переменная b = " + str(b))

print("2.4")
ispu = input("Введите фразу: ")
print("Строка:" + str(ispu) + ". " + "Длина: " + str(len(ispu)))

print("2.5")
word1 = input("Введите первое слово: ")
word2 = input("Введите первое слово: ")
bool1 = word1 in word2
bool2 = word1 == word2
bool3 = word1 > word2
bool4 = word1 < word2
print(str(bool1) + " " + str(bool2) + " " + str(bool3) + " " + str(bool4))

print("2.6")
letter1 = input("Введите первую букву: ")
letter2 = input("Введите вторую букву: ")
print("Коды: " + str(letter1) + " = "  + str(ord(letter1)) + ", " + str(letter2) + " = " + str(ord(letter2)))

print("2.7")
phase = input("Введите строку: ")
print(phase[0] + phase[len(phase)-1])

print("2.8")
phase = input("Введите строку: ")
print(phase[:4])

print("2.9")
phase = input("Введите строку: ")
phaselast = len(phase)
print(phase[phaselast-3:phaselast])

print("2.10")
phase = input("Введите строку: ")
phase_n = phase[1::2]
print(phase_n)

print("2.11")
str1 = input("Введите первую фразу: ")
str2 = input("Введите первую фразу: ")
print(str1[0::2] + " " + str2[1::2])

print("2.12")
phase = input("Введите строку: ")
phase_5 = phase[:5]
print(phase_5[::-1])

print("2.13")
word1 = input("Введите первое слово: ")
word2 = input("Введите первое слово: ")
print(word2[:(len(word1))])

print("2.14")
word1 = input("Введите первое слово: ")
word2 = input("Введите первое слово: ")
word1_new = word1[:(len(word2))]
index_word1n = word1_new[1::2]
index_word2 = word2[1::2]
print(index_word1n == index_word2)

print("2.15")
phase = input("Введите строку: ")
print(phase.capitalize())

print("2.16")
phase = input("Введите строку: ")
print("Число вхождений дефисов: ", phase.count('-'))

print("2.17")
phase = input("Введите строку: ")
print("Индекс первого вхождения ra:", phase.find('ra'))

print("2.18")
phase = input("Введите строку: ")
phase = phase.replace('---', '-')
phase = phase.replace('--', '-')
print("Результат:", phase)

print("2.19")
a = str(input("Введите первое число: "))
b = str(input("Введите второе число: "))
c = str(input("Введите третье число: "))
print("Результат: ", a.zfill(3), b.zfill(3), c.zfill(3))

print("2.20")
input_string = input("Введите строку: ")
words = input_string.split()
word_count = len(words)
print(word_count)

print("2.21")
input_string = input()
cities = input_string.split()
result = ';'.join(cities)
print(result)

print("2.22")
print('Тема занятия "спецсимволы"')
"""
print("2.23")
input_string = input()
words = input_string.split()
result = words[0] + '\\' + words[1]
print(result)

print("2.24")
input_string = input()
words = input_string.split(' ', 1)
result = words[0] + "'" + words[1].replace(' ', '"')
print(result)

print("2.25")


print("2.26")
name = input()
surname = input()
age = input()
print("Уважаемый {} {}! Поздравляем Вас с {}-летием!".format(name, surname, age))

print("2.27")
width = input()
depth = input()
height = input()
print("Габариты: {} x {} x {}".format(width, depth, height))

print("2.28")
a = int(input())
b = int(input())
print(f"{min(a, b)} {max(a, b)}")

print("2.29")
city = input()
street = input()
house = input()
apartment = input()
print(f"г. {city}, ул. {street}, д. {house}, кв. {apartment}")

print("2.30 ")
dollar_rate = float(input())
rubles = int(input())
dollars = int(rubles / dollar_rate)
print(f"Вы можете получить {dollars}$ за {rubles} рублей по курсу {dollar_rate}")

