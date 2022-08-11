def maskify(cc):
    result = ''
    for l in cc[::-1]:
        if len(result) >= 4:
            result += l.replace(l, '#')
        else:
            result += l
    return result[::-1]
    
    
    
    
    # return ''.join( cc.replace(l, "#") for l in cc[::-1] if len(cc)>4)
    # return "#"*(len(cc)-4) + cc[-4:]

print(maskify('SF$SDfgsd2eA'))