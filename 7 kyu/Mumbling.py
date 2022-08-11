def accum(s):
    result = ''
    n = 1
    for letter in s.lower():
        result += letter.upper()
        result += letter.lower() * (n - 1)
        result += '-'
        n += 1
     
    return result.strip('-')
