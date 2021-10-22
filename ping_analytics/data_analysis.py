import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ping_buffer import PingThread
from time import sleep

BUFFER_SIZE = 10

ping_buffer = [np.nan for _ in range(BUFFER_SIZE)]

pt = PingThread(ping_buffer, BUFFER_SIZE)
pt.start()

x = list(range(-BUFFER_SIZE // 2, BUFFER_SIZE // 2))
y = ping_buffer

fig, ax = plt.subplots()
ax.set_xlim(-BUFFER_SIZE / 2, BUFFER_SIZE / 2)
ax.set_ylim(0, 100)
line, = ax.plot(x,y)

# def init():  # give a clean slate to start
#     line.set_ydata([np.nan] * len(x))
#     return line,

# def animate(i):  # update the y values (every 1000ms)
#     line.set_ydata(y)
#     return line,

# ani = animation.FuncAnimation(fig, animate, init_func=init, interval=5, blit=True, save_count=10)

while True:
    y = ping_buffer
    line.set_ydata(y)
    plt.savefig('teste.png')
    sleep(1)







# with open("final.txt") as f:
#     c = 0
#     times = []
#     g50 = []
#     l50 = []
#     vecg = []
#     vecl = []
#     for line in f:
#         try: 
#             line = int(line)
#             c += 1
#             times.append(line)
#             if line > 50:
#                 g50.append(line)
#                 vecg.append(c)
#             else:
#                 l50.append(line)
#                 vecl.append(c)
#         except:
#             pass

# x = list(range(0, len(times)))

# fig, (ax1, ax2) = plt.subplots(2, 1)
# fig.suptitle('Horizontally stacked subplots')

# ax1.scatter(vecg, g50, color='r')
# ax1.scatter(vecl, l50, color='b')
# ax1.legend(["ping > 50 ms", "ping <= 50 ms"])
# ax1.set(xlabel="tempo", ylabel="ping")
# ax2.pie([len(g50), len(l50)], colors=['r', 'b'])
# ax2.legend(["ping > 50 ms", "ping <= 50 ms"])

# print("% de pings > 50 ms", round(len(g50) / (len(g50) + len(l50)), 4) * 100, "%")

# # sns.countplot(g50, l50)
# mpld3.show()