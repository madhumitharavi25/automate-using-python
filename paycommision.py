parentname = input() 
member = input()

if member == 'n' or member == 'N':
    print("TOTAL MEMBERS: 1") #printing parent member details
    print("COMMISION DETAILS:") #if no child member is present
    print(parentname,": 250 INR")
elif member == 'y' or member == 'Y':
    child = input()
    for i in child:       
        if i == " ":
            child1 = child.split(" ") #splitting the string by , or " "
        elif i == ",":
            child1 = child.split(",")
    
    #printing child member and parent member details
    print("TOTAL MEMBERS:",(len(child1)+1)) 
    print("COMMISION DETAILS:")
    print(parentname,":" + str(500 *len(child1)) + "INR")
    for i in child1:
        print(i,": 250 INR")        


