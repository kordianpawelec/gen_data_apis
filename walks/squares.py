import matplotlib.pyplot as plt

values = range(1,10001)
plot_values = [x**3 for x in values]

plt.style.use('seaborn-v0_8')

fig, ax,  = plt.subplots()

ax.scatter(values, plot_values, c=plot_values, cmap=plt.cm.BuGn_r)
# ax.plot(values, plot_values, c=plot_values, cmap=plt.cm.Blue, linewidth = 5)
#scatter()

ax.set_title('1,10000 cubed', fontsize=48)
ax.set_xlabel('values', fontsize=24)
ax.set_ylabel('cubes', fontsize=24)

ax.tick_params(labelsize = 24)
ax.axis([0,10100, 0, 1_500_000_000_000])
plt.ticklabel_format(style='scientific')


plt.show()