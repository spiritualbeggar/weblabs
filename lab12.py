print("12.1. Содержимое файла task12_1: ")
with open('lab12_txt/task12_1.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

print("12.2. Введите натуральное число (не более 8) для чтения первых n строк файла.")
n = int(input("Введите число: "))
with open('lab12_txt/task12_2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(n):
        print(lines[i].strip())

print("12.3. Содержимое файла task12_3.txt списком: ")
with open('lab12_txt/task12_3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)

print("12.4. Самые длинные слова task12_4.txt:")
with open('lab12_txt/task12_4.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    print(longest_words)

print("12.5. Количество строк в task12_4.txt: ")
with open('lab12_txt/task12_5.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(len(lines))

print("12.6. Частота слов в task12_6.txt: ")
from collections import Counter
with open('lab12_txt/task12_6.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    word_counts = Counter(words)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

print("12.7. Введите слова в строку через пробел: ")
words = input("Введите слова: ").split()
sorted_words = sorted(words)
with open('lab12_txt/task12_7.txt', 'w', encoding='utf-8') as file:
    for word in sorted_words:
        file.write(word + '\n')
with open('lab12_txt/task12_7.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

print("12.8. Введите слова в одну строку через пробел: ")
words = input("Введите слова: ")
with open('lab12_txt/task12_8.txt', 'a', encoding='utf-8') as file:
    file.write(words + '\n')
with open('lab12_txt/task12_8.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

print("12.9: Введите натуральное число")
max_length = int(input("Введите число: "))
with open('lab12_txt/task12_9_input.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()
    words = content.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
with open('lab12_txt/task12_9_output.txt', 'w', encoding='utf-8') as output_file:
    for line in lines:
        output_file.write(line + '\n')
with open('lab12_txt/task12_9_output.txt', 'r', encoding='utf-8') as output_file:
    content = output_file.read()
    print(content)

print("12.10. ")
from collections import defaultdict
import os
word_dict = defaultdict(list)
with open('lab12_txt/task12_10.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    for word in words:
        first_letter = word[0].upper()
        word_dict[first_letter].append(word)
if not os.path.exists('lab10_letters'):
    os.makedirs('lab10_letters')
for letter, words in word_dict.items():
    with open(f"lab10_letters/{letter}.txt", 'w', encoding='utf-8') as letter_file:
        for word in words:
            letter_file.write(word + '\n')
    print(f"Буква '{letter}': {len(words)} слов")