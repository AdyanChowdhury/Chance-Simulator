import random
import matplotlib.pyplot as plt

num_experiments = 100000
target_probab = 50.0

duplicate_probabilities = []
#generating birthdays
for j in range(1, 101):
    duplicate_count = 0
    group_size = j

    for _ in range(num_experiments):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        if len(birthdays) != len(set(birthdays)):
            duplicate_count += 1

    dupli_probab = round(duplicate_count / num_experiments * 100, 2)
    duplicate_probabilities.append(dupli_probab)
# Plotting the graph
group_sizes = list(range(1, 101))
plt.plot(group_sizes, duplicate_probabilities, marker='o', linestyle='-')
plt.xlabel("Group Size")
plt.ylabel("Probability of Duplicate Birthdays (%)")
plt.title("Probability of Duplicate Birthdays in Random Groups")
plt.grid(True)
plt.show()
