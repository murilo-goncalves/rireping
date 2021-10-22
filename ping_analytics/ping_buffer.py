import threading
from subprocess import call, run, PIPE
import re

class PingThread(threading.Thread):
    __ping_cmd = "ping 151.101.194.167 -c 1" # ping somewhere in SF

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

        if time_m is None: # ping failed
            return -1
 
        numeric_ping_m = re.search(r"[0-9]+\.[0-9]+", time_m.group())

        return numeric_ping_m.group()


    def __get_ping(self):
        cp = self.__run_bash_cmd(PingThread.__ping_cmd)
        ping_string = cp.stdout
        return float(self.__strip_ping_string(ping_string))


    def run(self):
        while True:
            self.ping_buffer.append(self.__get_ping())
            if (len(self.ping_buffer) > self.buffer_size):
                del self.ping_buffer[0]

if (__name__ == "__main__"):
    ping_buffer = []
    t = PingThread(ping_buffer, 5)
    t.start()
    while True:
        print(ping_buffer)