from math import sqrt
#functiion to check prime numbers
def PrimeisPrime(num):
    if num > 1:
        for i in range(2,int(sqrt(num)+1)): 
            if (num % i) == 0:
                return(False)
        else:
            return(True)

if __name__ == '__main__':    
    M = int(input())
    N = int(input())
    if (( (M>=2) and (M<=1000)) and ((N>M) and (N<=2000))): #given input constraint
        numbers = []
        for i in range(M,N+1): #appends the numbers for the given range
            numbers.append(i)
        result = list(map(PrimeisPrime, numbers)) # returns list having 'True' for the prime numbers else 'false'
        length = len(numbers) 
        #print(result)
        
        cntPairs = 0 
        #checks for the difference of 6
        for i in range(1,length):
            if((result [i] == True) and (result[i-6] == True) and ((i-6)>=0)):
                cntPairs+=1 #count the value if difference between is 6
        if (cntPairs>0):
            print(cntPairs)
        else:
            print("No Prime Pairs")
    
    else:
        quit()

