
def even_num(a):
    a = [2,3,4,5]
    for x in (a):
        if x % 2 == 0:
            a.append(x)
        else:
            print(x)
            
    return (a)
print(even_num(10))
