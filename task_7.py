import random
import matplotlib.pyplot as plt
import csv

analytical_probs = {
    2: "2.78% (1/36)",
    3: "5.56% (2/36)",
    4: "8.33% (3/36)",
    5: "11.11% (4/36)",
    6: "13.89% (5/36)",
    7: "16.67% (6/36)",
    8: "13.89% (5/36)",
    9: "11.11% (4/36)",
    10: "8.33% (3/36)",
    11: "5.56% (2/36)",
    12: "2.78% (1/36)"
}

def simulate_dice_throws(num_throws):
    results = [0] * 13
    for _ in range(num_throws):
        roll = random.randint(1, 6) + random.randint(1, 6)
        results[roll] += 1
    return results

def calculate_probabilities(results, num_throws):
    probabilities = [count / num_throws for count in results]
    return probabilities

num_throws = 100000
results = simulate_dice_throws(num_throws)
probabilities = calculate_probabilities(results, num_throws)

with open('dice_simulation.csv', 'w', newline='') as csvfile:
    fieldnames = ['sum', 'simulation_probability', 'analytical_probability']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for sum in range(2, 13):
        sim_prob = f"{probabilities[sum]*100:.2f}% ({results[sum]}/{num_throws})"
        ana_prob = analytical_probs[sum]
        writer.writerow({'sum': sum, 'simulation_probability': sim_prob, 'analytical_probability': ana_prob})

rows = []
with open('dice_simulation.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)

print(f"{'Сума':<4} {'Імітаційна ймовірність':<30} {'Аналітична ймовірність':<30}")
for row in rows:
    print(f"{row['sum']:<4} {row['simulation_probability']:<30} {row['analytical_probability']:<30}")

fig, ax = plt.subplots()
ax.bar(range(2, 13), probabilities[2:], align='center', alpha=0.5, label='Імітаційна ймовірність')
ax.bar(range(2, 13), [float(analytical_probs[sum].split()[0][:-1])/100 for sum in range(2, 13)], align='center', alpha=0.5, label='Аналітична ймовірність')

ax.set_xlabel('Сума')
ax.set_ylabel('Ймовірність')
ax.set_title('Ймовірність сум при киданні двох кубиків')
ax.set_xticks(range(2, 13))
ax.legend()

plt.show()