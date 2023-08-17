import random
num_experiments = 100000

allbdays = []
duplicate_count = 0
group_size = 23
for _ in range(num_experiments):
    birthdays = [random.randint(1, 365) for _ in range(group_size)]
    allbdays.append(birthdays)
    if len(birthdays) != len(set(birthdays)):
        duplicate_count += 1
dupli_probab = round(duplicate_count / num_experiments * 100, 2)
print[100]: duplicate_count
print("birthdays", allbdays)
print("duplicates=", duplicate_count)
print(" duplicate probability is", dupli_probab,"%")
