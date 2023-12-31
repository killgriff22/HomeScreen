import sys
import os
import subprocess
import hashlib
import time


def hash(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()


def load_config() -> dict:
    return exec(compile(open("config.py").read(), "config", "exec"))


def save_config(config: dict) -> None:
    with open("config.py", "w") as f:
        f.write(str(config))
    return


def print_at(x, y, content):
    command = f"\x1b7\x1b[{y};{x}f{content}\x1b8"
    sys.stdout.write(f"\x1b7\x1b[{y};{x}f{content}\x1b8")
    sys.stdout.flush()


def clear():
    os.system("clear")


class Fore:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'


class Back:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'


RESET = '\033[0m'


def info(message: str) -> None:
    return (f"{Fore.BLACK}{Back.BLUE}{message}{RESET}")


def warn(message: str) -> None:
    return (f"{Fore.BLACK}{Back.YELLOW}{message}{RESET}")


def error(message: str) -> None:
    return f"{Fore.BLACK}{Back.RED}{message}{RESET}"


def success(message: str) -> None:
    return (f"{Fore.BLACK}{Back.GREEN}{message}{RESET}")


def configure_safe_zone(display):
    w_base = 0
    h_base = 0
    while True:
        w, h = display.size
        screen = [[" "]*w for _ in range(h)]
        w -= 1
        h -= 1
        poses = [
            ((0+w_base), (0+h_base)), ((w)-w_base,  (h)-h_base), ((0) +
                                                                  w_base, (h)-h_base), ((w)-w_base,  (0)+h_base),
            ((1+w_base), (0+h_base)), ((w-1)-w_base,  (h)-h_base), ((1) +
                                                                    w_base, (h)-h_base), ((w-1)-w_base,  (0)+h_base),
            ((0+w_base), (1+h_base)), ((w)-w_base,  (h-1)-h_base), ((0) +
                                                                    w_base, (h-1)-h_base), ((w)-w_base,  (1)+h_base),
        ]
        for pos in poses:
            display.content[pos[1]][pos[0]] = "█"
        string = f"Current Size: {w-w_base},{h-h_base}"
        pos_x = w//2-len(string)//2
        pos_y = h//2
        for offset, char in enumerate(string):
            display.content[pos_y][pos_x+offset] = char
        # display.clear()
        display.draw()
