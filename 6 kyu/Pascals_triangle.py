import pysnooper

@pysnooper.snoop()
def pascals_triangle(n):
    p =[]
    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = p[i-1][j-1] + p[i-1][j]
        p.append(row)
    return  [x for y in p for x in y]


print(pascals_triangle(3))
