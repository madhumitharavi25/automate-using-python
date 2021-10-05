import re

def findnum(num,s):
    
    #function to find '9'
    def tofind(i):
        b = list(str(i))
        return True if '9' in b else i
    
    
    list_of_nums = list(map(int, re.findall('\d+', s))) # Extract numbers and cast them to int
    result = list(map(tofind, list_of_nums)) # maps to the tofind function


    if True in result:
        val = True
        result = [i for i in result if i != val]
        result.sort(reverse = True)
        return(result[0])

    else: #else sort and find the greatest number
        list_of_nums.sort(reverse = True)
        return(list_of_nums[0])


num = int(input())
if ( (num >= 1) and (num <= 100)): #given input constraints
    i = 1
    while (i <= num): 
        s = input()
        if (s != ''):
            if ((len(s)>=1) and (len(s)<=10000)): #given input constraints
                try:
                    print(findnum(num,s))
                except:
                    quit()
        else:
            print(-1)
        i += 1
    