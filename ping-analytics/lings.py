import matplotlib.pyplot as plt, mpld3
from threading import Thread
from subprocess import call, run, PIPE

# TODO: IMPLEMENTAR LOCKS PARA ARQUIVO

def get_pings():
    rc = call("./get_pings.sh")

def get_file_length():
    command = "wc -l ./pings.dat"
    c = command.split()
    result = run(c, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(int(result.stdout.split()[0]))
    return int(result.stdout.split()[0])

def limit_file_length(limit=int(10)):
    command = "sed -i '' '1d' pings.dat"
    c = command.split()
    file_len = get_file_length()
    if (file_len > limit):  
        result = run(c, stdout=PIPE, stderr=PIPE, universal_newlines=True)


thr = Thread(target=get_pings)
thr.start()

while True:
    limit_file_length()


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