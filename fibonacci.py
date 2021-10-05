def fibonacci(n):
    sum = 0
    final = 1
    array = []

    #finding the fibonacci series using
    #for loop.
    for i in range(0,n):
        new = final +sum
        array.append(new)
        final = sum
        sum = new
    print(array)
    count, number = 0,0
    for i in array:
        if ((i%2)==0): #counter for even number
            count = count+1
        else:    #counter for odd number
            number = number+1
    print(count)
    print(number)
    return array     

try:
    n = int(input())
    if ((n>5) and (n<=20)): #given input constraint
        fibonacci(n)  
    else:
        print("INVALID INPUT")
except:
    print("INVALID OUTPUT")
