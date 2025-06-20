import random

# Функція для симуляції підкидання двох гральних кісток задану кількість разів
def roll_dice(num_rolls):
    results = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        total = random.randint(1, 6) + random.randint(1, 6)
        results[total] += 1
    return results

# Обчислюємо ймовірність кожної суми
def probability(results, num_rolls):
    probabilities = {s: count / num_rolls for s, count in results.items()}
    return probabilities

# Головна функція для запуску симуляції та виведення результатів
def main():
    num_rolls = 100_000
    results = roll_dice(num_rolls)
    probabilities = probability(results, num_rolls)
    print("Сума\tЙмовірність")
    for total in sorted(probabilities):
        print(f"{total}\t{probabilities[total] * 100:.2f}%")


if __name__ == "__main__":
    main()