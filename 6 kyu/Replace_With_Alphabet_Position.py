import string


def alphabet_position(text):
    alphabet = string.ascii_lowercase
    result = ''
    for letter in text.lower():
        if alphabet.find(letter) == -1:
            
            continue
        result += str(alphabet.find(letter) + 1)
        result += ' '
    return result.strip(' ')
