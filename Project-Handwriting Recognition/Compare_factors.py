import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 3
means_neuro = (88.04347826086957, 81.30434782608695, 85.86956521739131)
means_agree = (87.39130434782608, 86.73913043478261, 85.21739130434782)
means_open  = (78.2608695652174, 79.78260869565217, 80.65217391304348)
means_cons  = (88.91304347826087, 88.26086956521739, 88.04347826086957)
means_extro = (87.39130434782608, 84.78260869565217, 86.30434782608696)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.1
opacity = 0.8

rects1 = plt.bar(index, means_neuro, bar_width, alpha=opacity, color='mediumturquoise', label='Neuroticism')
rects2 = plt.bar(index + bar_width, means_agree, bar_width, alpha=opacity, color='green', label='Agreeableness')
rects3 = plt.bar(index + bar_width + bar_width, means_open, bar_width, alpha=opacity, color='red', label='Openness')
rects4 = plt.bar(index + bar_width + bar_width + bar_width, means_cons, bar_width, alpha=opacity, color='gold', label='Conscientiousness')
rects5 = plt.bar(index + bar_width + bar_width + bar_width + bar_width, means_extro, bar_width, alpha=opacity, color='navy', label='Extroversion')

plt.xlabel('Algorithms')
plt.ylabel('Accuracy %')
plt.title('Comparison of Algorithms')
plt.xticks(index + bar_width + bar_width, ('Support Vector Machine', 'K-Nearest Neighbor', 'Random forest'))
plt.legend(loc = 'best', bbox_to_anchor=(0.2, -0.2))

plt.tight_layout()
plt.show()
