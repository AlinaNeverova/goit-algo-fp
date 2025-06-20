items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(budget):
    items_list = list(items.items())
    items_list.sort(key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True) # Сортуємо за співвідношенням калорії/вартість
    total_cost = 0
    total_calories = 0
    selected_items = []
    for item, details in items_list:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    return selected_items, total_cost, total_calories

# Динамічне програмування
def dynamic_programming(budget):
    n = len(items)
    items_list = list(items.items())
    dp = [0] * (budget + 1)
    selected = [[] for _ in range(budget + 1)]
    for i in range(n):
        item, details = items_list[i]
        cost = details['cost']
        calories = details['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                selected[b] = selected[b - cost] + [item]
    max_cal = max(dp)
    idx = dp.index(max_cal)
    return selected[idx], idx, max_cal

# Основна функція для тестування
def main():
    budget = 100

    print("Greedy Algorithm:")
    selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(budget)
    print(f"Selected items: {selected_items_greedy}")
    print(f"Total cost: {total_cost_greedy}, Total calories: {total_calories_greedy}")

    print("\nDynamic Programming:")
    selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(budget)
    print(f"Selected items: {selected_items_dp}")
    print(f"Total cost: {total_cost_dp}, Total calories: {total_calories_dp}")

if __name__ == "__main__":
    main()