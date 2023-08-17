import random
num_experiments = 100000

duplicate_count = 0
group_size = 20
for _ in range(num_experiments):
    birthdays = [random.randint(1, 365) for _ in range(group_size)]
    if len(birthdays) != len(set(birthdays)):
        duplicate_count += 1
print("duplicates=", duplicate_count)
