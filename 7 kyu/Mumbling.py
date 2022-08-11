def accum(s):
    result = ''
    n = 1
    for letter in s.lower():
        # result += letter.upper() + ''.join([char for char in range((s.lower()).index(letter))])
        result += letter.upper()
        result += letter.lower() * (n - 1)
        result += '-'
        n += 1
     
    return result.strip('-')


print(accum('abcd'))
# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))
#     # Python 3.4 solution || you don't need to import anything :)
#     # return dna.translate(str.maketrans("ATCG","TAGC"))
# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])