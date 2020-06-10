class Text:
    text = input("Input text, please")  # Sentences must be split by ". "


class Sentences:
    sentences = Text.text.split(". ")


class Words:
    words = input("Input words, please!")  # Words must be split by ", "


class Letters:
    # Letters is a clear class, because in my variant don`t use letters.
    pass


class PunctuationMarks:
    # PunctuationMarks is a clear class, because in my variant don`t use punctuation marks.
    pass


class Main:
    lst_text = Text.text.split(". ")
    lst_words = Words.words.split(", ")
    result = list()
    for i in lst_words:
        k = 0
        for j in lst_text:
            if i in j:
                k += 1
        result.append(i + " : " + str(k))


print(Main.result)
