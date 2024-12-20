def Generate_Table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)
    for char in alphabet:
        if char not in table:
            table.append(char)
    return table


def Playfair_Cipher_E(input_text, key):
    table = Generate_Table(key)
    input_list = list(input_text.upper().replace("j", "i"))
    for i in range(0, len(input_list), 2):
        if input_list[i] == input_list[i + 1]:
            input_list.insert(i + 1, 'X')
    if len(input_list) % 2 == 1:
        input_list.append('X')

    output = ''
    for i in range(0, len(input_list), 2):
        index1 = table.index(input_list[i])
        index2 = table.index(input_list[i + 1])

        if abs(index1 - index2) == abs(index1 % 5 - index2 % 5):
            output += table[(index1 + 1) % 5]
            output += table[(index2 + 1) % 5]
        elif index1 % 5 == index2 % 5:
            output += table[(index1 + 5) % 25]
            output += table[(index2 + 5) % 25]
        else:
            output += table[(index1 + 1) % 5]
            output += table[(index2 + 1) % 5]

    return output


def Playfair_Cipher_D(input_text, key):
    table = Generate_Table(key)
    input_list = list(input_text.upper())
    output = ''
    for i in range(0, len(input_list), 2):
        index1 = table.index(input_list[i])
        index2 = table.index(input_list[i + 1])

        if abs(index1 - index2) == abs(index1 % 5 - index2 % 5):
            output += table[(index1 - 1) % 5]
            output += table[(index2 - 1) % 5]
        elif index1 % 5 == index2 % 5:
            output += table[(index1 - 5) % 25]
            output += table[(index2 - 5) % 25]
        else:
            output += table[(index1 - 1) % 5]
            output += table[(index2 - 1) % 5]

    return output

