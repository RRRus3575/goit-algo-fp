items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for x in range(budget + 1)] for x in range(n + 1)]
    item_list = list(items.keys())
    
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            cost = items[item_list[i-1]]['cost']
            calories = items[item_list[i-1]]['calories']
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_list[i-1])
            w -= items[item_list[i-1]]['cost']
    
    return selected_items, dp[n][budget]




budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm Result:")
print("Selected Items:", greedy_result[0])
print("Total Calories:", greedy_result[1])

dp_result = dynamic_programming(items, budget)
print("Dynamic Programming Result:")
print("Selected Items:", dp_result[0])
print("Total Calories:", dp_result[1])
