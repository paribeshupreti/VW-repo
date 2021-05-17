#Problem 1 find the sum of all the multiples of 3 and 5 below 1000

def mul(x):

    sum = 0

    for i in range(x):

        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i 

    return sum
    


#Problem 2. find the sum of the even-valued terms of the fib sequence that do not exceed 40000





def fib(index):

    sum = 0

    if index == 0:
        return 0
    if index == 1:
        return 1 
    
    else:
        return fib(index - 1) + fib(index - 2)


   

    

        

print(fib(10))


    




