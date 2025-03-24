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
        line = input()
        parts = line.split()
    
        #if else statements
        if parts[0] == 'PASS':
            #set current passkey
            print('pass')
        elif parts[0] == 'ENCRYPT':
            #encrypt parts[1] with current passkey and output result
            #if no passkey then pass error
            print('encrypt')
        elif parts[0] == 'DECRYPT':
            #decrypt argument with current passkey and output result
            #if no passkey then pass error
            print('decrypt')
        elif parts[0] == 'QUIT':
            #exit program go back to driver
            break
        else:
            print("ERROR invalid command")


if __name__ == "__main__":
    main()