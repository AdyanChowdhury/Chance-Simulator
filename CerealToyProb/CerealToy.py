import random
import numpy as np
import matplotlib.pyplot as plt

def test(NumTrials, toys_list):
    results = []

    for _ in range(NumTrials):
        toyscollected = {toy: 0 for toy in toys_list}
        total_boxes = 0

        while True:
            total_boxes += 1
            toy = random.choice(toys_list)
            toyscollected[toy] += 1

            if sum(1 for count in toyscollected.values() if count >= 2) == len(toys_list):
                results.append(total_boxes)
                break

    return results

toys_list = [4, 5, 7, 8]
trials = test(10000, toys_list)

# Histogram
plt.hist(trials, bins=20)
plt.axvline(np.mean(trials), color="tab:red", linestyle="dashed", label="mean")
plt.axvline(np.median(trials), color="tab:green", linestyle="dashed", label="median")
plt.xlabel("Boxes Opened")
plt.ylabel("Number Of Trials")
plt.legend()
plt.show()

# Boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(trials, vert=False)
plt.xlabel("number of boxes opened")
plt.yticks([])
plt.title("Boxplot of Trials")
plt.show()