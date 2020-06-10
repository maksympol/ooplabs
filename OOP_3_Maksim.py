"""Задано текст та масив слів. Підрахувати у скількох реченнях зустрічається кожне слово масиву."""
text = input("Input text, please!")  # Sentences must be split by ". "
words = input("Input words, please!")  # Words must be split by ", "
lst_text = text.split(". ")
lst_words = words.split(", ")
result = list()
for i in lst_words:
    k = 0
    for j in lst_text:
        if i in j:
            k += 1
    result.append(i + " : " + str(k))
print(result)

