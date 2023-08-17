import random
birthdays = []
people = 20
for i in range(1, people):
  birthdays.append(random.randint(0, 365))

print(birthdays)