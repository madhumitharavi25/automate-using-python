from math import sqrt
def PrimeisPrime():
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                
if __name__ == '__main__':    
    M = int(input())
    N = int(input()) 
    numbers = []
    for i in range(M,N+1):
        numbers.append(i)
    result = list(map(PrimeisPrime, numbers))
    length = len(numbers)
    print(cntPairsdiffOfPrimeisPrime(M,numbers,N))

