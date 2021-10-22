import matplotlib.pyplot as plt
import mpld3
import threading
from subprocess import call, run, PIPE
import re

# TODO: IMPLEMENTAR LOCKS PARA ARQUIVO

class PingThread(threading.Thread):
    __ping_cmd = "ping 151.101.194.167 -c 1"

    def __init__(self, ping_buffer, buffer_size):
        threading.Thread.__init__(self)
        self.ping_buffer = ping_buffer
        self.buffer_size = buffer_size

    def __run_bash_cmd(self, cmd):
        cmd = cmd.split()
        cp = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        return cp

    def __strip_ping_string(self, ping_string):
        time_m = re.search(r"time=[^ ]*", ping_string)
        numeric_ping_m = re.search(r"[0-9]+\.[0-9]+", time_m.group())
        return(numeric_ping_m.group())

    def __get_ping(self):
        cp = self.__run_bash_cmd(PingThread.__ping_cmd)
        ping_string = cp.stdout
        return float(self.__strip_ping_string(ping_string))


    def run(self):
        while True:
            self.ping_buffer.append(self.__get_ping())
            if (len(self.ping_buffer) > self.buffer_size):
                del self.ping_buffer[0]
            print(self.ping_buffer)


ping_buffer = []
t = PingThread(ping_buffer, 10)
t.start()

# def get_file_length():
#     command = "wc -l ./pings.dat"
#     c = command.split()
#     result = run(c, stdout=PIPE, stderr=PIPE, universal_newlines=True)
#     print(int(result.stdout.split()[0]))
#     return int(result.stdout.split()[0])

# def limit_file_length(limit=int(10)):
#     command = "sed -i '' '1d' pings.dat"
#     c = command.split()
#     file_len = get_file_length()
#     if (file_len > limit):  
#         result = run(c, stdout=PIPE, stderr=PIPE, universal_newlines=True)


# thr = Thread(target=get_pings)
# thr.start()

# while True:
#     limit_file_length()


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