import subprocess
import re
from threading import Thread

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
        print(COMPLIENCE)

main()
