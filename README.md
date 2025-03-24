# vigenere
#File Organization:
This repository should hold 6 files: 3 for the actual program (driver.py, encrypt,py, logger,py), a logger file for this program (log_file.txt), a readme.md, and a devlog.md. Keep these files in the same directory to ensure the program runs correctly. I will break down the files and any assumptions I made in the following passages.

#Driver.py:
This file holds the driver program for this project, so this is the program you will be running. This program begins by accepting the log file from the command line, which I already have created (log_file.txt). This program then creates the pipes for connecting this program to the logger.py and encrypt.py files using the subprocess module before displaying a menu of choices (password, encrypt, decrypt, history, quit) for a user to choose from. Password sets the key for the menu's current cycle using a key from the history or a new key, which also gets set as a passkey in the encrypt.py file. Afterwards, you can choose from encrypt or decrypt which uses the select passkey in ecnrypting/decrypting using a Vigenère cipheron alphabetic characters. Selecting history will display a list of the past encrypted and decrypted strings to choose from in case the user doesn't want to input a new string. Selecting quit will end all three programs.

#Encrypt.py:
This file holds two functions: vigenere_cipher and main. vigenère_cipher has the code for completing the cipher while main has the choices that align with the driver's menu. This program reads input from the driver program's menu choices and either sets a key, encrypts a string, decrypts a string, or quits. Its output is written in the command line through the driver program.

#Logger.py:
This file has two functions: logger(log_file, log_message) and main. The logger function does the actual logging to the log file by taking the datetime module and using it to display the date and time while writing an inputted log message to the right of it. The main function reads the log file's name and reads log messages from the driver program and runs them through the logger function which prints them to the log file. In the event of a quit command from the driver program, this program will also quit and print a quit and ending program statement to the log file.

#Log_file.txt:
This is an empty file that will eventually hold the log messages printed by the logger.py file in the form "Year-month-day hour:minute log_message". To have the best results, this file should be cleared before running a new execution of the programs.

#devlog.md:
This file holds my devlog that I wrote in describing the work I did in each session. Its headers are the date and time of each entry. Entries written before a session have 2 elements: any developments/thoughts heading into the session and the goal for the sessions. Entries written after a session have three elemenets: problems encountered during the session, if the previously mentioned goal was accomplished and why/why not, and what the goal of the next session is. Entries written during a session outline indiviudal problems encountered and their solution.

#Running the program:
To run the program, ensure that driver.py, encrypt.py, logger.py, and log_file.txt are all in the same directory. Open the driver.py file and run it. Once running, it should ask for the name of the log file, which would be "log_file.txt". Once its name is  inputted, it should display a menu of choices and directions for each choice on how to proceed. Once done with the program, type in quit as a menu choice. Ensure passkeys are written in uppercase and all strings only use alphabetic characters or else there will be an error message.

