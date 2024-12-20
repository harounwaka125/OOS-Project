import math

def columnar_encrypt(text, key):
    text = text.replace(" ", "")
    cipherText = [""] * key
    for row in range(key):
        pointer = row
        while pointer < len(text):
            cipherText[row] += text[pointer]
            pointer += key
    return "".join(cipherText)


def columnar_decrypt(textplain, key):
    textplain = textplain.replace(" ", "")
    text = [""] * key
    position_first_character = 0
    colum = 0
    number_of_columns_with_character = len(textplain) % key if len(textplain) % key != 0 else key

    while position_first_character < len(textplain):
        c = position_first_character
        position_first_character += math.ceil(len(textplain) / key)
        while c != position_first_character:
            if c == len(textplain):
                break
            text[colum] += textplain[c]
            c += 1
        number_of_columns_with_character -= 1
        colum += 1
    textplain = ""
    pointer = 0
    while pointer < len(text[0]):
        for i in range(key):
            textplain += text[i][pointer]
        pointer += 1
    return textplain

