text = input("Введите текст на русском языке: ")

voiced_consonants = "бвгджзлмнрй"

found_consonants = []

for char in text.lower():
    if char in voiced_consonants and char not in found_consonants:
        found_consonants.append(char)

found_consonants.sort()
print("Звонкие согласные буквы, которые входят хотя бы в одно слово текста:", found_consonants)