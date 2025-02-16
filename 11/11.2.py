sentence1 = input("Введите первое предложение: ")
sentence2 = input("Введите второе предложение: ")

words1 = sentence1.split()
words2 = sentence2.split()

set1 = set(words1)
set2 = set(words2)

common_words = set1.intersection(set2)

for word in common_words:
    cleaned_word = word.strip(".,!?")
    print(cleaned_word)