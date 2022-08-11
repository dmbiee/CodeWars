def find_short(s):
    s = s.split()   
    return len(sorted(s, key=len)[0]) # l: shortest word length

print(find_short('helloasdasd as asfasfa a word!'))