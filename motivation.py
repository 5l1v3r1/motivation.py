logo = """                  _   _            _
  _ __ ___   ___ | |_(_)_   ____ _| |_ ___   _ __  _   _
 | '_ ` _ \ / _ \| __| \ \ / / _` | __/ _ \ | '_ \| | | |
 | | | | | | (_) | |_| |\ V / (_| | ||  __/_| |_) | |_| |
 |_| |_| |_|\___/ \__|_| \_/ \__,_|\__\___(_) .__/ \__, |
                                            |_|    |___/ """

print(logo)
import string, csv
from time import *
from colorama import Fore, init, Back
from datetime import datetime


def formatTime(x):
        minutes, seconds_rem = divmod(x, 60)
        return "%02d:%02d" % (minutes, seconds_rem)

music_list = ['0.Concentration \ Programming Music 000 : https://www.youtube.com/watch?v=svngvOLPd5E',
              '1.Concentration \ Programming Music 001 : https://www.youtube.com/watch?v=pmxYePDPV6M',
              '2.Concentration \ Programming Music 002 : https://www.youtube.com/watch?v=Pwrhzfsq8t4',
              '3.Concentration \ Programming Music 003 : https://www.youtube.com/watch?v=5CLFwCUyWqY',
              '4.Concentration \ Programming Music 004 : https://www.youtube.com/watch?v=1Uw7tmg2hwk',
              "5.Concentration \ Programming Music 005 : https://www.youtube.com/watch?v=c5X4-pCDy94"
              ]
init(autoreset=True)
print('Script is starting...\n'.center(40))
sleep(0.3)
print('Ready?\n'.center(40))
sleep(0.3)
first = int(input((Fore.BLUE + "How long will you work?(* type as minute):\n")))
sleep(0.1)
second = input(str((Fore.YELLOW + "Do you want to save this session(as .csv file) (y/n):\n")))
sleep(0.1)
if second.lower() == 'y':
    record_name = input(str((Fore.BLUE + "Write the session name: \n")))
    sleep(0.1)
    idea = input(str((Fore.RED + 'What do you want to do? Write your idea: \n')))
    with open('{0}.csv'.format(record_name), 'w') as csvfile:
        fieldnames = ['Session Name', 'Idea', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Session Name': record_name, 'Idea': idea, 'Time': str(datetime.now())})
        sleep(0.1)
        print((Fore.YELLOW + '[+] File saved as {0}.csv \n'.format(record_name)))
else:
    print(Fore.WHITE + 'Okay, im jumping...\n')
sleep(0.1)
music = input(str((Fore.GREEN + "Want some music? I can show you a natural playlist (y/n):\n")))
sleep(0.1)
if music.lower() == 'y':
    for i in music_list:
        print((Fore.GREEN + i))
        sleep(0.1)
    else:
        pass
sleep(0.1)
start = input(str((Fore.WHITE + "Want to start? Type 'Enter' \n")))
sleep(0.1)
for x in range(first * 60, -1, -1):
    sleep(1)
    print(formatTime(x))

print((Fore.RED + "[+] Your time has finished. You've done great! Dude, work hard!"))