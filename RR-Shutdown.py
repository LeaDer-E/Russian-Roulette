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

def shutdown_system():
    """
    Shutdown the computer based on the operating system.
    NOTE: Some commands may require administrative privileges.
    """
    os_name = platform.system()
    try:
        if os_name == "Windows":
            os.system("shutdown /s /t 0")
        elif os_name == "Linux":
            os.system("shutdown -h now")
        elif os_name == "Darwin":  # macOS
            os.system("osascript -e 'tell app \"System Events\" to shut down'")
        else:
            print(Fore.RED + "Unsupported OS for shutdown command." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error shutting down system: {e}" + Style.RESET_ALL)

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

print_banner()
print(Fore.YELLOW + "*" * 104 + Style.RESET_ALL)
time.sleep(0.5)

print(Fore.GREEN + "Welcome to Computer Russian Roulette! 🎮" + Style.RESET_ALL)
time.sleep(0.5)
print(Fore.GREEN + "You have 3 attempts to guess the correct number (1-6)." + Style.RESET_ALL)
print(Fore.RED + "Pick the correct number, and your PC will shutdown immediately! 😈" + Style.RESET_ALL)
print(Fore.MAGENTA + "*" * 104 + Style.RESET_ALL)
time.sleep(0.5)

# Randomly choose the "shutdown number"
shutdown_number = random.randint(1, 6)
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
    
    # If the guess matches the shutdown number, initiate shutdown
    if guess == shutdown_number:
        print(Fore.RED + "💀 You chose the correct number! Your PC will now shutdown..." + Style.RESET_ALL)
        # Optionally, play the alarm sound before shutdown
        play_alarm()
        shutdown_system()
        break
    else:
        print(Fore.BLUE + random.choice(survival_messages) + Style.RESET_ALL)
        time.sleep(0.5)

# If the player did not trigger shutdown during their attempts
if guess != shutdown_number:
    print(Fore.GREEN + "Congratulations! You survived all attempts and won! 🏆" + Style.RESET_ALL)

print(Fore.YELLOW + "*" * 104 + Style.RESET_ALL)
