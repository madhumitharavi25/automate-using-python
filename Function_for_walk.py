#Function for walk
def is_valid_walk(walk):
    string = "".join(walk)
    #print(string)
    list = []
    for i in string:
        list.append(ord(i))
    #print(list)
    #print(len(list))
    north = 0
    south = 0
    west = 0
    east = 0
    for i in list:
        if i == ord('n'):
            north = north + 1
        if i == ord('s'):
            south = south +1 
        if i == ord('e'):
            east = east +1 
        if i == ord('w'):
            west = west +1        
    if len(list) != 10:
        return False
    elif north == south and east == west:
        return True
    else:
        return False
    