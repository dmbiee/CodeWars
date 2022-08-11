def maskify(cc):
    result = ''
    for l in cc[::-1]:
        if len(result) >= 4:
            result += l.replace(l, '#')
        else:
            result += l
    return result[::-1]
