from os import listdir, system
from os.path import isfile, join
import subprocess
import time


class rekt:
    def __init__(self):
        self.library = self.get_library()
        self.index = 0
        self.appnd = "./library/"
        self.thread = None
        self.rep = "play-audio"

    def reproduce(self):
        self.thread = subprocess.Popen([self.rep +
                                        " \"" +
                                        self.appnd +
                                        self.library[self.index] +
                                        "\" 2> /dev/null"],
                                       shell=True)
        if self.index == len(self.library)-1:
            self.index = 0
        else:
            self.index = self.index + 1

    def get_library(self):
        return [f for f in listdir("./library")
                if isfile(join("./library", f))]

    def stop(self):
        self.thread.terminate()

    def next(self):
        self.stop()
        self.reproduce()


if __name__ == '__main__':
    re = rekt()
    re.reproduce()

    try:
        while True:
            raw_input()
            re.next()
    except Exception:
        re.stop()
