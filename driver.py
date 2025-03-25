import sys
from subprocess import Popen, PIPE

def main():
    
    log_file = input("Input log file name: ")

    log = Popen(["python", "logger.py", log_file], stdin=PIPE, encoding='utf8')
    encrypt = Popen(["python", "encrypt.py"], stdin=PIPE, stdout=PIPE, encoding='utf8')

    log.stdin.write("[START] Driver program started\n")
    log.stdin.flush()

    history = []
    passkey = None

    #Print menu
    while True:
        print("""
        password
        encrypt
        decrypt
        history,
        quit
        """)

        choice = input("Enter command: ").lower()
        log.stdin.write(f"[COMMAND] {choice}\n")
        log.stdin.flush()

        #if command is password
        if choice == "password":
            #pick between password from history or ask user to add create new string
            pwchoice = input("Pick 'history' or 'new': ")
            log.stdin.write(f"[PASSWORD] Pick 'history' or 'new': {pwchoice}\n ")
        
            #new password
            if pwchoice =="new":
                text = input("Enter new passkey: ")
                password = text.upper()
                encrypt.stdin.write(f"PASS {password}\n")
                encrypt.stdin.flush()

            #old password
            elif pwchoice == "history":
                #create history
                for i, item in enumerate(history):
                    print(f"{i+1}: {item}")
                index = int(input("Select index: ")) - 1
                passkey = history[index]
            else:
                print("Invalid choice")

        #if command is encrypt
        elif choice == "encrypt":
            #if no password set then go back to menu
            if password is None:
                print("ERROR password not set")
                continue
            #pick old or new string to encrypt
            enchoice = input("Pick 'history' or 'new' string: ")
            #new string
            if enchoice == "new":
                txt = input("Enter new string: ")
                #only allow alphabetic characters in string
                if not text.isalpha():
                    print("Error: Only letters allowed.")
                    continue
                encrypt.stdin.write(f"ENCRYPT {text}\n")
                encrypt.stdin.flush()
                history.append(text)
                
            #old string
            elif enchoice == "history":
                #print history
                for i, item in enumerate(history):
                    print(f"{i+1}: {item}")
                index = int(input("Select index: ")) - 1
                encrypt.stdin.write(f"ENCRYPT {text}\n")
                encrypt.stdin.flush()
                history.append(text)
                #allow user to pick from history

            else:
                print("Error: Invalid encryption choice")

        #if command is decrypt
        elif choice == "decrypt":
            if password is None:
                print("Output: ERROR password not set")
                continue

            dechoice = input("Pick 'history' or 'new' string: ")
            #if decrypting new string
            if dechoice == "new":
                txt = input("Enter new string: ")
                if not text.isalpha():
                    print("Error: Only letters allowed.")
                    continue
                encrypt.stdin.write(f"DECRYPT {text}\n")
                encrypt.stdin.flush()
                history.append(text)
                print(encrypt.stdout.readline.rstrip())
                    
            #if decrypting old string
            elif dechoice == "history":
                #print menu
                for i, item in enumerate(history):
                    print(f"{i+1}: {item}")
                index = int(input("Select index: ")) - 1
                encrypt.stdin.write(f"DECRYPT {text}\n")
                encrypt.stdin.flush()
                history.append(text)
                #allow user to pick a string
            else:
                print("ERROR Invalid decryption choice")

        #if command is history
        elif choice == "history":
            print("History:")
            for item in history:
                print(item)

        #if command is quit
        elif choice == "quit":
            encrypt.stdin.write("QUIT NOW\n")
            encrypt.stdin.flush()
            log.stdin.write("[QUIT] Exiting program\n")
            log.stdin.flush()

            encrypt.wait()
            log.wait()
            break

        else:
            print("ERROR Invalid choice")
            log.stdin.write("[ERROR] Invalid command\n")
            log.stdin.flush()

if __name__ == "__main__":
    main()

























        