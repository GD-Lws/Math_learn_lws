import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)
cmap = get_cmap(30)
fig = plt.figure()
ax_1 = fig.add_subplot(441)  # 创建子图
plt.xlim(0, 2890)
plt.ylim(0, 1230)
plt.plot([2440, 2440], [0, 1220], linewidth=1, color='black')
plt.plot([0, 2440], [1220, 1220], linewidth=1, color='black')
plt.text(1049, 290, '1')
rect = plt.Rectangle((0, 0), 2098, 580, color=cmap(9))  # （0.1，0.2）为左下角的坐标，0.4，0.3为宽和高，负数为反方向，红色填充
ax_1.add_patch(rect)

ax_2 = fig.add_subplot(442)
plt.xlim(0, 2890)
plt.ylim(0, 1230)
plt.plot([2440, 2440], [0, 1220], linewidth=1, color='black')
plt.plot([0, 2440], [1220, 1220], linewidth=1, color='black')
plt.text(1049, 290, '1')
rect = plt.Rectangle((0, 0), 2098, 580, color="red")  # （0.1，0.2）为左下角的坐标，0.4，0.3为宽和高，负数为反方向，红色填充
ax_2.add_patch(rect)

plt.show()
