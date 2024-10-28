def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


data = input("13.1. Введите данные через пробел: ")
data_list = data.split()
integer_sum = sum(map(int, filter(is_integer, data_list)))
print("Сумма целых чисел:", integer_sum)
def convert_value(value):
    try:
        if '.' in value or 'e' in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


data = input("13.2. Введите данные через пробел: ")
data_list = data.split()
converted_list = list(map(convert_value, data_list))
print("Преобразованный список:", converted_list)
data = input("13.3. Введите два значения через пробел: ")
values = data.split()
try:
    first_value = float(values[0])
    second_value = float(values[1])
    result = first_value + second_value
except ValueError:
    result = values[0] + values[1]
finally:
    print("Результат:", result)
