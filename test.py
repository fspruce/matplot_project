import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.ylabel('some numbers')
plt.show()

name = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(name, values)
plt.subplot(132)
plt.scatter(name, values)
plt.subplot(133)
plt.plot(name, values)
plt.suptitle('Categorical Plotting')
plt.show()
