import matplotlib.pyplot as plt
import numpy as np
import math

cores = ('teal', 'mediumaquamarine', 'lightsteelblue', 'tomato', 'midnightblue', 'cornflowerblue', 'bisque')

thresh_total = np.array(   [0.001, 0.01, 0.20, 0.30, 0.50, 0.80, 0.82, 0.84, 0.86, 0.88, 0.89, 0.90, 0,92, 0.95, 0.98, 0.99])
precision_total = np.array([0, 0.55, 0.85, 0.98, 0.98, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 1.00, 1.00, 1.00, 1.00, 1])
recall_total = np.array(   [1, 0.99, 0.99, 0.98, 0.98, 0.97, 0.93, 0.91, 0.90, 0.89, 0.86, 0.84, 0.82, 0.78, 0.66, 0.36, 0.12, 0])

plt.figure(1)
#plt.figure(figsize=(4,4))
plt.plot(recall_total, precision_total, cores[0], linewidth=3)
plt.xlabel("Sensibilidade")
plt.ylabel("Precisão")
plt.xlim([0, 1.02])
plt.ylim([0, 1.02])
plt.grid(True)
plt.savefig('img-resultados-pr-total.pdf')

thresh = np.array(   [0.001, 0.01, 0.1, 0.4,  0.8,  0.9, 0.95,  0.98, 0.99])
precision = np.array([[ 0.51, 0.84, 0.95, 0.96, 0.99, 0.98, 1.00, 1.00, 1.00, 1],
                     [ 0.62, 0.96, 0.99, 0.99, 0.99, 1.00, 1.00, 1.00, 1.00, 1],
                     [ 0.65, 0.93, 0.98, 0.98, 0.99, 0.99, 1.00, 1.00, 1.00, 1],
                     [ 0.37, 0.64, 0.98, 0.99, 1.00, 1.00, 0.99, 1.00, 1.00, 1],
                     [ 0.54, 0.85, 0.96, 0.98, 0.99, 0.99, 1.00, 1.00, 1.00, 1],
                     [ 0.73, 0.96, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1]])
recall = np.array(   [[ 0.97, 0.97, 0.97, 0.97, 0.95, 0.83, 0.54, 0.26, 0.01, 0],
                     [ 0.99, 0.99, 0.99, 0.98, 0.94, 0.76, 0.62, 0.25, 0.02, 0],
                     [ 1.00, 1.00, 0.99, 0.98, 0.90, 0.71, 0.55, 0.18, 0.02, 0],
                     [ 0.97, 0.97, 0.95, 0.93, 0.82, 0.71, 0.53, 0.30, 0.06, 0],
                     [ 0.99, 0.99, 0.99, 0.99, 0.98, 0.95, 0.81, 0.49, 0.20, 0],
                     [ 1.00, 1.00, 1.00, 1.00, 1.00, 0.96, 0.89, 0.68, 0.36, 0]])
classes = ("circuito aberto", "curto-circuito", "falta de cobre", "excesso de cobre", "trilha desconectada", "falta de estanho")

plt.figure(2)
#plt.figure(figsize=(4,4))
#plt.plot(precision_total, recall_total, cores[6], label="Todas as Classes", linewidth=10)
for i in range(6):
  plt.plot(recall[i], precision[i], cores[i], label=classes[i], linewidth=2)
plt.legend(loc="lower left")
plt.xlabel("Sensibilidade")
plt.ylabel("Precisão")
plt.xlim([0, 1.02])
plt.ylim([0, 1.02])
plt.grid(True)
plt.savefig('img-resultados-pr.pdf')
