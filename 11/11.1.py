text = input("Введите текст, заканчивающийся точкой: ")

words = text.split()

for word in words:
    cleaned_word = word.strip(".,!?")
    if len(cleaned_word) == 3:
        print(cleaned_word)