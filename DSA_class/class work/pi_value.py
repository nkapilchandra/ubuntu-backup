import random
import matplotlib.pyplot as plt

inside = 0
total = 0
pi_values = []
for i in range(10000):
    x = random.random()
    y = random.random()
    if x**2 + y**2 < 1:
        inside += 1
        total += 1
    else:
        total += 1
    pi_values.append(4.0*inside/total)

print(pi_values[-1])
plt.plot(pi_values)
plt.show()
