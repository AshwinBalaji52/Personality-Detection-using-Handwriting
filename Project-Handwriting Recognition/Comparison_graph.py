import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.style.use('seaborn-whitegrid')
import numpy as np

my_paper = [88.043, 87.391, 80.652, 88.913, 87.391, 85.128]
base_paper = [85.3, 80.5, 80, 88.3, 87.4, 80.5]

plt.plot(base_paper, '-o', color='r')
plt.plot(my_paper, '-o', color='navy')

base_patch = mpatches.Patch(color='red', label='Prior Art')
my_patch = mpatches.Patch(color='navy', label='Current Art')
plt.legend(handles=[base_patch, my_patch])

plt.ylabel('Accuracy %')
plt.xlabel('Neuroticism  Agreeableness  Openness  Conscientiousness  Extraversion  Overall Accuracy')
plt.show()
