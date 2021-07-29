# Initializing the values of cps into a list  
CPS= ['MH04CC2', 'MH04C2820', 'MH04BB3232', 'MH04CC2113', 'MH04CC2878', 'MH04BB8', 
'MH04CC1313', 'MH04CC2222', 'MH04C1201', 'MH04CC555', 'MH04C6565', 'MH04A7']

#getting the input from the user (Input should be '1' or '2)
number = int(input())


#Functions used for searching car_plate number  
#enumerate function is used to control the starting value of the count. 

# Below funtion used to search
def search(car_number1):
    for park1, i in enumerate(CPS, 1):
        if car_number1 == i:
            return park1
    return -1

# Below function used to allocate a new position
def plate(car_number2):
    global CPS # changes will be made globally
    CPS.append(car_number2) #append the new input car number 
    for park2,i in enumerate(CPS, 1):
        if car_number2 == i:
            return (park2)
    return -1

#Directing the input to the right function
if number != 1 and number != 2:
    print("Invalid Input")    


else:
    car_number = input()
    is_valid = False
    #checking the length of the input
    if (len(car_number)>=6) and (len(car_number)<12):
        is_valid = True    
        
    # If option 2 is selected the search is made with the CPS using for loop
    if number == 2 and is_valid:
        park1 = search(car_number) # calling the search function
        if park1>0:
            print("CAR POSITION:", park1)
        else: 
            print("car doesn't exists")
    
    #If option 1 is selected then it finds the new position for the car after the last position
    elif number == 1 and is_valid:
        park2 = plate(car_number) # calling the plate function
        if park2>0:
            print("CAR POSITION:", park2)
        else: 
            print("Invalid input")
    else:
        print("Invalid input")
