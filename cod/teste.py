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
