from collections import Counter

answers = ["кошка", "собака", "кошка", "дракон", "собака", "кошка", "дракон", "дракон", "кошка"]
N = len(answers)
k = 2

answer_counts = Counter(answers)

most_common = answer_counts.most_common(k)

for answer, count in most_common:
    percentage = (count / N) * 100
    print(f"Ответ: {answer}, Частота: {percentage:.2f}%")