'''def add_numbers():
   total = 0
   for number in range(1, 10 + 1):
       print(number)
       total = total + number
   return(total)    
answer = add_numbers()
print(answer)
'''
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
    for i in range(start,end + 1):
        print(i)
        start = start + i
    end = start
    return(end) 

test1 = add_numbers(1,2)
print(test1)
test2 = add_numbers(1, 100)
print(test2)
test3 = add_numbers(1000, 5000)
print(test3)
