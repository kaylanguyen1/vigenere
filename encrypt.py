import sys

def vigenere_cipher(text, key, decrypt=False):
    if not key:
        return None
    key = key.lower()
    key_length = len(key)
    key_shifts = [ord(k) - ord('a') for k in key]
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = key_shifts[key_index % key_length]
            if decrypt:
                shift = -shift
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result.append(new_char)
                key_index += 1
        else: 
            result.append(char)
    return ''.join(result)

def main():
    passkey = "hello"

    
    while True:
        line = sys.stdin.readline().strip()
        parts = line.split()
        if len(parts) < 2:
            print("ERROR invalid command")
            sys.stdout.flush()
            continue

        command = parts[0]
        argument = parts[1]

    
        #if else statements
        if parts[0] == 'PASS':
            #set current passkey
            passkey = argument
            print("RESULT")
        elif parts[0] == 'ENCRYPT':
            #encrypt parts[1] with current passkey and output result
            #if no passkey then pass error
            if not passkey:
                print("ERROR Passkey not set")
            else:
                print("RESULT", vigenere_cipher(argument, passkey))
        elif parts[0] == 'DECRYPT':
            #decrypt argument with current passkey and output result
            #if no passkey then pass error
            if not passkey:
                print("ERROR Passkey not set")
            else:
                print("RESULT", vigenere_cipher(argument, passkey, decrypt=True))
        elif parts[0] == 'QUIT':
            #exit program go back to driver
            print("RESULT Quit")
            sys.stdout.flush()
            break
        else:
            print("ERROR invalid command")
        sys.stdout.flush()

if __name__ == "__main__":
    main()