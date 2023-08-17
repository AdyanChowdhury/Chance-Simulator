import random
num_experiments = 100000
duplicate_probabilities = []
for j in range(1, 101):
    duplicate_count = 0
    group_size = j

    for _ in range(num_experiments):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        if len(birthdays) != len(set(birthdays)):
            duplicate_count += 1

    dupli_probab = round(duplicate_count / num_experiments * 100, 2)
    duplicate_probabilities.append(dupli_probab)

    print(f"For Group_Size={group_size}")
    print(f"duplicates={duplicate_count}")
    print(f"duplicate probability is: {dupli_probab}%\n")

print("List of duplicate probabilities:", duplicate_probabilities)