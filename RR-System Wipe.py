import random
import time
import os
import platform
from colorama import init, Fore, Style
import pygame
import shutil

def ensure_terminal_size(min_width=104):
    """
    Ensures that the terminal width is at least the specified minimum.
    """
    while True:
        width = shutil.get_terminal_size().columns
        if width >= min_width:
            return
        print(f"\n[!] Terminal too small! Please resize it to at least {min_width} columns, Increase Width please.")
        time.sleep(2)  # Wait for user to resize

ensure_terminal_size()

# Initialize colorama for colored terminal output
init()

# Initialize pygame for playing sound
pygame.mixer.init()

# Check if the alarm sound file exists
alarm_file = "alarm.wav"
if not os.path.exists(alarm_file):
    print(Fore.RED + f"Error: '{alarm_file}' not found. Please place an 'alarm.wav' file in the same directory." + Style.RESET_ALL)
    exit()

def simulate_removal():
    """
    Simulates the deletion of system files without actually deleting anything.
    The messages displayed do not reveal that this is a simulation until the end.
    """
    # Determine the file paths based on the operating system
    if os.name == "nt":  # Windows
        username = os.environ.get("USERNAME", "User")
        files_to_delete = [
            "C:\\Windows",
            "C:\\Program Files",
            "C:\\Program Files (x86)",
            "C:\\Users",
            "C:\\Windows\\System32",
            "C:\\Windows\\SysWOW64",
            f"C:\\Users\\{username}\\AppData",
        ]
    elif os.uname().sysname == "Darwin":  # macOS
        base_path = "/"
        files_to_delete = [
            f"{base_path}bin",
            f"{base_path}usr/bin",
            f"{base_path}sbin",
            f"{base_path}usr/sbin",
            f"{base_path}System/Library",
            f"{base_path}Library",
            f"{base_path}Applications",
            f"{base_path}Users",
        ]
    else:  # Linux
        base_path = "/"
        files_to_delete = [
            f"{base_path}bin",
            f"{base_path}sbin",
            f"{base_path}lib",
            f"{base_path}boot",
            f"{base_path}usr/bin",
            f"{base_path}usr/sbin",
            f"{base_path}usr/lib",
            f"{base_path}etc",
            f"{base_path}var",
            f"{base_path}home",
            f"{base_path}root",
        ]
    
    # Display initial warning message
    print("\n⚠️ WARNING: System wipe initiated! ⚠️\n")
    time.sleep(2)

    # Print deletion messages with a suspense effect
    for item_path in files_to_delete:
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Deleting: {item_path}")
    
    time.sleep(1)
    print("\n💀 System wipe complete! 💀")
    # Reveal that this was just a simulation
    time.sleep(1)
    print("\nRevealing: This was just a simulation. Your files remain intact! 😊\n")

def play_alarm():
    """
    Plays the alarm sound.
    """
    try:
        pygame.mixer.music.load(alarm_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)  # Wait until the sound finishes playing
        print(Fore.RED + "Alarm sound played successfully!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error playing sound: {e}" + Style.RESET_ALL)

def print_banner():
    """
    Prints the game banner.
    """
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

# Print banner and decorative separator
print_banner()

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


print(Fore.YELLOW + "*" * 104 + Style.RESET_ALL)
time.sleep(0.5)

# Display welcome messages
print(Fore.GREEN + "Welcome to Computer Russian Roulette! 🎮" + Style.RESET_ALL)
time.sleep(0.5)
print(Fore.GREEN + "You have 3 attempts to guess the correct number (1-6)." + Style.RESET_ALL)
print(Fore.RED + "Pick the correct number, and your PC will undergo a system wipe! 😈" + Style.RESET_ALL)
print(Fore.MAGENTA + "*" * 104 + Style.RESET_ALL)
time.sleep(0.5)

# Randomly choose the wipe number that triggers the simulated system wipe
wipe_number = random.randint(1, 6)
used_numbers = []  # Track numbers that have been chosen

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

# Main game loop (3 attempts)
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
    
    # If the guess matches the wipe number, initiate the simulated system wipe
    if guess == wipe_number:
        print(Fore.RED + "💀 You chose the correct number! Initiating system wipe..." + Style.RESET_ALL)
        # Play the alarm sound before starting the simulation
        play_alarm()
        simulate_removal()
        break
    else:
        print(Fore.BLUE + random.choice(survival_messages) + Style.RESET_ALL)
        time.sleep(0.5)

# If the player did not trigger the wipe during their attempts
if guess != wipe_number:
    print(Fore.GREEN + "Congratulations! You survived all attempts and won! 🏆" + Style.RESET_ALL)

print(Fore.YELLOW + "*" * 104 + Style.RESET_ALL)
