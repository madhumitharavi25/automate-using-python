# Python program to remove vowels from a string
# Function to remove vowels
import re
def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    
    #checking for consonants
    result = [letter for letter in string if letter.lower() not in vowels]
    
    #checking for vowels
    result2 =[letter for letter in string if letter.lower() in 'a']
    result3 =[letter for letter in string if letter.lower() in 'e']
    result4 =[letter for letter in string if letter.lower() in 'i']
    result5 =[letter for letter in string if letter.lower() in 'o']
    result6 =[letter for letter in string if letter.lower() in 'u']
    
    #printing the number of vowels 
    print( 'a:'+ str(len(result2)),'\ne:'+str(len(result3)),'\ni:'+str(len(result4)),'\no:'+ str(len(result5)),'\nu:' +str(len(result6)) )
    
    result = ''.join(result) 
    print(result) #printing except vowels
    return(result)
 
# Driver program
string = input()
if string != "":
    vowels = ['a','e','i','o','u']
    list_of_nums = list(map(int,re.findall("\d+",string)))
    result = [letter for letter in string if letter.lower() in vowels]
    #print(len(result))
    if((len(list_of_nums))> 0):
        print("0")
    else:
        if((len(result) > 0)):
            rem_vowel(string)
        else:
            print("0")
else:
    print("INVALID INPUT")
