def count(string):
    dic = dict()
    for l in string:
        dic.update({l : string.count(l)})
    return dic
