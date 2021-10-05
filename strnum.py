import re

def findnum(num,s):
    
    #function to find '9'
    def tofind(i):
        b = list(str(i))
        return True if '9' in b else None
    
    list_of_nums = list(map(int, re.findall('\d+', s))) # Extract numbers and cast them to int
    result = list(map(tofind, list_of_nums)) # maps to the tofind function 

    if True in result:  # if true then prints the another number
        for i in range(0,len(result)):
            if result[i] is not True:
                return(list_of_nums[i])

    else: #else sort and find the greatest number
        list_of_nums.sort(reverse = True)
        return(list_of_nums[0])


num = int(input())
if ( (num >= 1) and (num <= 100)):
    i = 1
    while (i <= num): 
        s = input()
        if (s != ''):
            if ((len(s)>=1) and (len(s)<=10000)): #given input constraints
                print(findnum(num,s))
        else:
            print(-1)
        i += 1
    