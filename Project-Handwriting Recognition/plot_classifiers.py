import matplotlib.pyplot as plt
import numpy as np


label = ['Support Vector Machine', 'K-Nearest Neighbor', 'Random Forest']
y_pos = np.arange(len(label))
performance = [88.04347826086957,81.30434782608695, 85.86956521739131]
fig,ax = plt.subplots()
bars = plt.bar(y_pos, performance, align='center', alpha=0.5, color = ["red", "blue", "green"])
plt.xticks(y_pos, label)

# access the bar attributes to place the text in the appropriate location
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .005, yval)
plt.ylabel('Predicted Accuracy')
plt.title('Neuroticism : Comparing Classifiers')


plt.show()

#---------------------------------------------------------------------------------

label = ['Support Vector Machine', 'K-Nearest Neighbor', 'Random Forest']
y_pos = np.arange(len(label))
performance = [87.39130434782608,86.73913043478261, 85.21739130434782]
fig,ax = plt.subplots()
bars = plt.bar(y_pos, performance, align='center', alpha=0.5, color = ["red", "blue", "green"])
plt.xticks(y_pos, label)

# access the bar attributes to place the text in the appropriate location
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .005, yval)
plt.ylabel('Predicted Accuracy')
plt.title('Agreeableness : Comparing Classifiers')

plt.show()

#---------------------------------------------------------------------------------

label = ['Support Vector Machine', 'K-Nearest Neighbor', 'Random Forest']
y_pos = np.arange(len(label))
performance = [78.2608695652174, 79.78260869565217, 80.65217391304348]
fig,ax = plt.subplots()
bars = plt.bar(y_pos, performance, align='center', alpha=0.5, color = ["red", "blue", "green"])
plt.xticks(y_pos, label)

# access the bar attributes to place the text in the appropriate location
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .005, yval)
plt.ylabel('Predicted Accuracy')
plt.title('Openness : Comparing Classifiers')

plt.show()

#---------------------------------------------------------------------------------

label = ['Support Vector Machine', 'K-Nearest Neighbor', 'Random Forest']
y_pos = np.arange(len(label))
performance = [88.91304347826087, 88.26086956521739, 88.04347826086957]
fig,ax = plt.subplots()
bars = plt.bar(y_pos, performance, align='center', alpha=0.5, color = ["red", "blue", "green"])
plt.xticks(y_pos, label)

# access the bar attributes to place the text in the appropriate location
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .005, yval)
plt.ylabel('Predicted Accuracy')
plt.title('Conscientiousness : Comparing Classifiers')

plt.show()

#--------------------------------------------------------------------------------

label = ['Support Vector Machine', 'K-Nearest Neighbor', 'Random Forest']
y_pos = np.arange(len(label))
performance = [87.39130434782608,  84.78260869565217, 86.30434782608696]
fig,ax = plt.subplots()
bars = plt.bar(y_pos, performance, align='center', alpha=0.5, color = ["red", "blue", "green"])
plt.xticks(y_pos, label)

# access the bar attributes to place the text in the appropriate location
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .005, yval)
plt.ylabel('Predicted Accuracy')
plt.title('Extraversion : Comparing Classifiers')

plt.show()
