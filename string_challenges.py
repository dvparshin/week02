# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"Последняя буква в слове {word}: {word[-1]}")


# Вывести количество букв "а" в слове
word = 'Архангельск'
desired_letter = 'а'
letter_count = 0
for letter in word:
    if desired_letter in letter:
        letter_count += 1
print(f"Буква {desired_letter} встречается {letter_count} раз в слове {word}")


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
vowel_count = 0
for letter in word:
    if letter in vowels:
        vowel_count += 1
print(f"Количество гласных букв в слове {word}: {vowel_count}")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f"Количество слов в предложении: {len(sentence.split())}")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
cout_latter = len(sentence.replace(' ', ''))
coutn_word = len(sentence.split())
avg_word_len = cout_latter / coutn_word
print(f"Усреднённая длина слова в предложении: {int(avg_word_len)}")