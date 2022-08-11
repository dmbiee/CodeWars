def heron(a, b, c):
    s = (a + b + c)/2
    heron = (s*(s-a)*(s-b)*(s-c))**(0.5)
    return round(heron, 2)