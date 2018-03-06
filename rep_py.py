import sys
sys.path.insert(0, "./app")
import os
import curses
import time
from rekt import rekt

rep = False

def show_songs(size,
               screen,
               rep_list):
    init = int(size["height"] * 0.1)
    tail = int(size["height"] - init*2)
    aux = 0
    for k in range(init, tail):
        if aux <= (len(rep_list)-1):
            screen.addstr(k,
                          0,
                          rep_list[aux])
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
            rep_list):
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
            rk = rekt()
            rep_list = rk.library
            rk.reproduce()

            while True:
                refresh(screen, rep_list)
                char = screen.getch()
                if char == ord('q'):
                    break
                elif char == ord('p'):
                    rk.stop()
                elif char == ord('s'):
                    rk.reproduce()
                else:
                    rk.next()
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
