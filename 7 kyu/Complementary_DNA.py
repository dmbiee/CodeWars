def DNA_strand(dna):
    key = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    result = ''
    for letter in dna:
        if letter in key:
            result += key[letter]
    return result
print(123123)