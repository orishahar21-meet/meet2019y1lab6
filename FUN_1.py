'''def jamie_HW():
    start = 333
    for end in range(333, 777 + 1):
        print(end)
        start = start + end
    end = start
    return(end)    
answer = jamie_HW()
print(answer)
'''
def add_numbers(start, end):
    sum1 = 0
    for i in range(start,end + 1):
        #print(i)
        sum1 = sum1 + i
    return(sum1)

test1 = add_numbers(1,2)
print(test1)

test2 = add_numbers(1, 100)
print(test2)

test3 = add_numbers(1000, 5000)
print(test3)

'''home_w = add_numbers(333,777)
print(home_w)
'''
