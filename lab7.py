
n = int(input("7.1 Введите целое положительное число: "))
squares_dict = {}
for i in range(1, n + 1):
    squares_dict[i] = i ** 2
print(squares_dict)

print("7.2 Введите данные в формате ключ=значение: ")
data = input().split()
d = dict(item.split('=') for item in data)
d = {key: int(value) for key, value in d.items()}
print(*sorted(d.items()))

data = input("Задание 7.3. Введите данные в формате ключ=значение через пробел: ").split()
d = {int(item.split('=')[0]): item.split('=')[1] for item in data}
print(*sorted(d.items()))

data = input("Задание 7.4. Введите данные в формате ключ=значение через пробел: ").split()
d = dict(item.split('=') for item in data)
if 'house' in d and 'True' in d and '5' in d:
    print("Yes")
else:
    print("No")

data = input("Задание 7.5. Введите номера телефонов через пробел: ").split()
d = {}
for number in data:
    code = number[:2]
    if code not in d:
        d[code] = []
    d[code].append(number)
print(*sorted(d.items()))

d = {}
while True:
    entry = input("Задание 7.6. Введите номер и имя через пробел (или 0 для завершения): ").split()
    if entry[0] == '0':
        break
    number, name = entry[0], entry[1]
    if name not in d:
        d[name] = []
    d[name].append(number)
print(*sorted(d.items()))

cache = {}
while True:
    num = int(input("Задание 7.7. Введите целое положительное число (или 0 для завершения): "))
    if num == 0:
        break
    if num in cache:
        print(f"значение из кэша: {cache[num]}")
    else:
        sqrt_value = round(num ** 0.5, 2)
        cache[num] = sqrt_value
        print(sqrt_value)

morse_code = {
    'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': ' '
}
input_str = input("Задание 7.8. Введите строку на русском языке: ").lower()
encoded_str = ' '.join(morse_code[char] for char in input_str)
print(encoded_str)

morse_decode = {
    '.-': 'а', '-...': 'б', '.--': 'в', '--.': 'г', '-..': 'д', '.': 'е', '...-': 'ж', '--..': 'з', '..': 'и', '.---': 'й', '-.-': 'к', '.-..': 'л', '--': 'м', '-.': 'н', '---': 'о', '.--.': 'п', '.-.': 'р', '...': 'с', '-': 'т', '..-': 'у', '..-.': 'ф', '....': 'х', '-.-.': 'ц', '---.': 'ч', '----': 'ш', '--.-': 'щ', '--.--': 'ъ', '-.--': 'ы', '-..-': 'ь', '..-..': 'э', '..--': 'ю', '.-.-': 'я', ' ': ' '
}
input_morse = input("Задание 7.9. Введите закодированную строку азбукой Морзе: ").split()
decoded_str = ''.join(morse_decode[code] for code in input_morse)
print(decoded_str)

d = {}
while True:
    entry = input("Задание 7.11. Введите день рождения и имя через пробел (или 0 для завершения): ").split()
    if entry[0] == '0':
        break
    day, name = entry[0], entry[1]
    if day not in d:
        d[day] = []
    d[day].append(name)
for day in sorted(d.keys()):
    print(f"{day}: {', '.join(d[day])}")

items = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200, 'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
max_weight = int(input("Задание 7.12. Введите максимальный вес в кг: ")) * 1000
sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
taken_items = []
current_weight = 0
for item, weight in sorted_items:
    if current_weight + weight <= max_weight:
        taken_items.append(item)
        current_weight += weight
print(' '.join(taken_items))

input_str = input("Задание 7.13. Введите строку: ")
d = {char: input_str.count(char) for char in input_str}
print(d)
