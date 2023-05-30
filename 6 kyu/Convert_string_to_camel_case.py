def to_camel_case(text):
    if text == '' or text == None:
        return

    string = text.replace("-", " ").replace("_", " ")
    string = string.split()
    if len(text) == 0:
        return text
    return string[0] + ''.join(i.capitalize() for i in string[1:])
