import numpy as np
import matplotlib.pyplot as plt
import math

cores = ('teal', 'mediumaquamarine', 'chocolate', 'tomato', 'midnightblue', 'gold')

#SIGMOIDE
x_sig = np.linspace(-5, 5, num=100)
y_sig = 1/(1+np.exp(-x_sig))
plt.figure(0)
#plt.rcParams.update({"text.usetex": True, "font.family": "serif", "font.serif": ["Palatino"],})
plt.figure(figsize=(2.5,2.5))
plt.plot(x_sig, y_sig, cores[0], linewidth=2)
plt.gcf().subplots_adjust(left=0.25)
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel("z")
plt.ylabel("f(z)")
plt.grid(True)
plt.savefig('img-fundamentacao-sig.pdf')

#TANH
x_tan = np.linspace(-5, 5, num=100)
y_tan = np.tanh(x_sig)
plt.figure(1)
#plt.rcParams.update({"text.usetex": True, "font.family": "serif", "font.serif": ["Palatino"],})
plt.figure(figsize=(2.5,2.5))
plt.plot(x_tan, y_tan, cores[0], linewidth=2)
plt.gcf().subplots_adjust(left=0.25)
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel("z")
plt.ylabel("f(z)")
plt.grid(True)
plt.savefig('img-fundamentacao-tanh.pdf')

#RELU
x_relu = np.linspace(-5, 5, num=100)
y_relu = np.zeros(100)
y_relu[50:100] = x_relu[50:100]
plt.figure(2)
#plt.rcParams.update({"text.usetex": True, "font.family": "serif", "font.serif": ["Palatino"],})
plt.figure(figsize=(2.5,2.5))
plt.plot(x_relu, y_relu, cores[0], linewidth=2)
plt.gcf().subplots_adjust(left=0.25)
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel("z")
plt.ylabel("f(z)")
plt.grid(True)
plt.savefig('img-fundamentacao-relu.pdf')

#MISH
x_mish = np.linspace(-5, 5, num=100)
y_mish = x_mish * np.tanh(np.log(1+np.exp(x_mish)))
plt.figure(2)
#plt.rcParams.update({"text.usetex": True, "font.family": "serif", "font.serif": ["Palatino"],})
plt.figure(figsize=(2.5,2.5))
plt.plot(x_mish, y_mish, cores[0], linewidth=2)
plt.gcf().subplots_adjust(left=0.25)
plt.gcf().subplots_adjust(bottom=0.3)
plt.xlabel("z")
plt.ylabel("f(z)")
plt.grid(True)
plt.savefig('img-fundamentacao-mish.pdf')
