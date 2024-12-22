# caeser encreption
def Caesar_Cipher_E(input_text, key):
    output = ''
    for char in input_text:
        if char.isupper():
            output += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            output += chr((ord(char) + key - 97) % 26 + 97)
        else:
            output += char
    return output
# caeser decreption 

def Caesar_Cipher_D(input_text, key):
    output = ''
    for char in input_text:
        if char.isupper():
            output += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            output += chr((ord(char) - key - 97) % 26 + 97)
        else:
            output += char
    return output

# sohaila 
