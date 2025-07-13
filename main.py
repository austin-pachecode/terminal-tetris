import curses
from game import run

if __name__ == "__main__":
    curses.wrapper(run)