n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())

if n <= 0 or j<=0:
    print("INVALID INPUT")

#/* calculating remaining bananas and Peanuts */
else:
    rem1 = m%k
    rem2 = p%j
    banana = int(m/k)
    peanut = int(p/j)

#/* calculating monkeys in the tree */
    if((rem1 == 0) and (rem2 == 0)):
        num = (n - (banana + peanut))

    elif((rem1!=0) or (rem2 != 0)):
        num = (n - (banana + peanut)-1)
    
    if(num <= 0):
        print("Invalid Input") #* If there is a negative output then the given input condition is not possible */ 
    
    else:
        print("Number of Monkeys left on the Tree: ",num)