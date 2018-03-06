import sys
import os
import curses
from os import listdir
from os.path import isfile, join
import threading
import time
from pygame import mixer
import mutagen.mp3

rep = False


def get_library():
    return [f for f in listdir("./library") if isfile(join("./library", f))]


def show_songs(size,
               screen,
               rep_list):
    init = int(size["height"] * 0.1)
    tail = int(size["height"] - init*2)
    library = get_library()
    aux = 0
    for k in range(init, tail):
        if aux <= (len(library)-1):
            screen.addstr(k,
                          0,
                          library[aux])
        aux = aux + 1
    screen.refresh()


def show_head(size,
              screen):
    screen.addstr(0,
                  0,
                  "@autor: dcpulido91@gmail.com")
    screen.refresh()


def show_tail(size,
              screen):
    pass


def clear_window(size, screen):
    for k in range(0,
                   size["height"]):
        sst = ""
        for h in range(0,
                       size["width"]-1):
            sst = sst + " "
        screen.addstr(k,
                      0,
                      sst)
        screen.refresh()


def get_window_size(screen):
    height, width = screen.getmaxyx()
    return dict(height=height,
                width=width)


def sleeper(tm):
    rep = True
    time.sleep(tm)
    rep = False


def refresh(screen,
            rep_list,
            index):
    sizes = get_window_size(screen)
    clear_window(sizes, screen)
    show_head(sizes, screen)
    show_songs(sizes, screen, rep_list)
    show_tail(sizes, screen)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        os.system("cd ./library && "
                  "youtube-dl --extract-audio "
                  "--audio-format mp3 " +
                  sys.argv[1] +
                  " && cd ../")
    else:
        try:
            screen = curses.initscr()
            curses.noecho()
            curses.cbreak()
            screen.keypad(True)
            rep_list = get_library()
            index = 0
            thread = None
            init = True

            while True:
                refresh(screen, rep_list, index)
                char = screen.getch()
                if char == ord('q'):
                    break
                elif char == curses.KEY_UP or rep == False or init == True:
                    """
                    mp3 = mutagen.mp3.MP3("./library/"+rep_list[index])
                    mixer.init(frequency=mp3.info.sample_rate)
                    mixer.music.load("./library/"+rep_list[index])
                    if index == len(rep_list)-1:
                        index = 0
                    else:
                        index = index + 1
                    mixer.music.play()
                    """
                    t1 = threading.Thread(target=os.system(
                        "play-audio \"./library/"+rep_list[index]))
                    t1.start()
                elif char == curses.KEY_DOWN:
                    t1._Thread__stop()
                    fl = False
                    if init == True:
                        init = False
                    else:
                        init = True
                elif char == ord('r'):
                    pass
        except Exception as e:
            raise e
            curses.nocbreak()
            screen.keypad(0)
            curses.echo()
            curses.endwin()
        finally:
            curses.nocbreak()
            screen.keypad(0)
            curses.echo()
            curses.endwin()
