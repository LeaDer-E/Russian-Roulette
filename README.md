# Computer Russian Roulette Repository

**Game Overview:**  
Welcome to Computer Russian Roulette – a high-stakes simulation game that brings an authentic adrenaline rush! The scripts in this repository not only mimic dangerous system operations such as a system wipe, shutdown, restart, and even closing all open applications, but they also recreate the tension and excitement of a risky game. When you try out the "real" file (RR-Real.py), you'll experience a surge of adrenaline as it simulates an actual deletion process. **Remember, this is only a simulation for educational purposes – never run these scripts on a real system!**

---

## Contents

- **RR-System Wipe.py**  
  Simulates a system wipe by faking the deletion of critical files without performing any real deletion.

- **RR-Shutdown.py**  
  Simulates shutting down the computer by executing the appropriate system commands.

- **RR-Restart.py**  
  Simulates restarting the computer by executing the appropriate system commands.

- **RR-KillAll.py**  
  Simulates closing all open applications (logging out of the system).

- **RR-Alarm.py**  
  Plays an alarm sound when the player loses in the game.

- **RR-Real.py**  
  **SEVERE WARNING:** This is the real deletion script. It attempts to delete a set of critical files and directories based on the operating system using Python's `os.remove` function. Running this script may lead to permanent data loss and system corruption.

  > **Warning:** This script is for educational purposes only. **Do not run it on any real system.** It is strongly recommended to place this script in a separate folder within the repository along with its own README file that reiterates this warning.

---

## Detailed Explanation of the Real Deletion Script (RR-Real.py)

### Purpose:
The **RR-Real.py** script is designed to delete a set of system-critical files and folders depending on the operating system (Windows, macOS, or Linux). The deletion is performed using `os.remove`, and if executed on a real system, it can cause irreversible damage.

### How It Works:
1. **Terminal Size Check:**  
   The script ensures that the terminal window is wide enough (at least 104 columns) to display messages correctly.

2. **Library Initialization:**  
   It initializes libraries like `colorama` for colored terminal output and `pygame` for playing an alarm sound.

3. **Alarm File Verification:**  
   The script checks for the presence of an `alarm.wav` file in the same directory. If the file is missing, the script exits.

4. **Deletion Process:**  
   - Depending on the operating system, the script compiles a list of critical file and directory paths.
   - For each path, it checks if the file or directory exists.
   - If it exists, the script attempts to delete it using `os.remove`, displaying success or error messages accordingly.

### **Strict Warning:**
- **DO NOT run this script on any actual system.**  
  Running **RR-Real.py** may permanently delete essential system files, leading to system failure or data loss.
- This script is provided solely for educational and experimental purposes.  
  If you wish to study or test it, do so in a completely isolated environment (e.g., a virtual machine) that does not contain critical data.
- **Usage on production or personal systems is strongly discouraged.**

---

## How the Code Works and How to Run It

### How the Code Works:
- **Terminal Check:**  
  Each script begins by verifying that the terminal window is wide enough (at least 104 columns) to properly display output.
  
- **Library Initialization:**  
  The code initializes necessary libraries, such as `colorama` for colored terminal output and `pygame` for playing alarm sounds.
  
- **Alarm File Verification:**  
  Before executing any main functionality, the scripts check for the existence of an `alarm.wav` file. If it’s not found, the script exits to avoid errors.
  
- **Game Mechanics:**  
  Most scripts implement a game loop where the user is prompted to guess a number between 1 and 6 in three attempts. Depending on the guess:
  - A simulated action is triggered (e.g., system wipe simulation, shutdown, restart, logout).
  - In the case of **RR-Real.py**, if the correct number is chosen, the script attempts to delete critical system files (which is why it should never be run on a real system).
  
- **Visual and Audio Feedback:**  
  The scripts display colorful banners and messages to enhance the game experience and play an alarm sound upon triggering the main action.

### How to Run the Code:
1. **Prerequisites:**
   - **Python 3:** Ensure you have Python 3 installed on your system.
   - **Dependencies:** Install the required libraries by running:
     ```bash
     pip install colorama pygame
     ```
   - **Alarm File:** Place an `alarm.wav` file in the same directory as the scripts.

2. **Running a Script:**
   - Open a terminal and navigate to the repository directory.
   - Run the desired script using the following command:
     ```bash
     python RR-System\ Wipe.py
     ```
     Replace `RR-System Wipe.py` with the script you wish to execute (e.g., `RR-Shutdown.py`, `RR-Restart.py`, etc.).
   - Follow the on-screen instructions to play the game.

3. **Caution:**
   - **Do Not Run RR-Real.py on a Real System:**  
     The RR-Real.py script performs real file deletion operations. It is intended for educational purposes only and should be run only in a safe, isolated environment (such as a virtual machine).
   - Always review the warnings and understand the code before execution.

---

## General Instructions for All Scripts

- **Alarm File:**  
  Ensure that the `alarm.wav` file is present in the same directory as the scripts for the alarm sound to work correctly.
  
- **Execution Environment:**  
  It is recommended to run these scripts in a testing or virtualized environment rather than on a system that contains real or critical data.
  
- **Purpose:**  
  All scripts are designed for educational and entertainment purposes. Read and understand the instructions and warnings before executing any script.

