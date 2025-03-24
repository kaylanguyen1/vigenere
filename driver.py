import sys

def main():
    
    log_file = input("Input log file name: ")

    #Print menu
    while True:
        print("""
        password
        encrypt
        decrypt
        history
        quit
        """)
        command = input("Enter command:").lower()

        #if command is password
        if command == "password":
            #pick between password from history or ask user to add create new string
            pwchoice = input("Pick 'history' or 'new': ")
            #new password
            if pwchoice =="new":
                text = input("Enter new passkey: ")
                password = text.upper()

            #old password
            elif pwchoice == "history":
                #create history
                pass
            else:
                print("Invalid choice")

        #if command is encrypt
        elif command == "encrypt":
            #if no password set then go back to menu
            if password is None:
                print("Output: ERROR password not set")
                continue
            #pick old or new string to encrypt
            enchoice = input("Pick 'history' or 'new' string: ")
            #new string
            if enchoice == "new":
                txt = input("Enter new string: ")
                #only allow alphabetic characters in string
                if not txt.isalpha():
                    print("Error: Only letters allowed.")
                    continue
            #old string
            elif enchoice == "history":
                pass
                #print history
                
                #allow user to pick from history
            else:
                print("Error: Invalid encryption choice")
        #if command is decrypt
        elif command == "decrypt":
            if password is None:
                print("Output: ERROR password not set")
                continue
            dechoice = input("Pick 'history' or 'new' string: ")

            #if decrypting new string
            if dechoice == "new":
                txt = input("Enter new string: ")
                if not txt.isalpha():
                    print("Error: Only letters allowed.")
                    continue
                    
            #if decrypting old string
            elif dechoice == "history":
                pass
                #print menu
                
                #allow user to pick a string
            else:
                print("ERROR Invalid decryption choice")

        #if command is history
        elif command == "history":
            print("History:")

        #if command is quit
        elif command == "quit":
            break

        else:
            print("ERROR Invalid choice")

if __name__ == "__main__":
    main()

























        