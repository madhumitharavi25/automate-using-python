#Getting the input from the user
N = input()
M = str(N)
k = float(N)
#d = float('.'.join((N.split('.'))))

#Converting it to a list and splitting it with '.' 
# so to get the hour and minutes 
# the hour and minutes are converted to int datatype using map function 
# and stored in a list 
M = list(map(int,M.split('.')))


if M[0]>= 23:
    new = (M[0]-23.00)
else:
    new = (M[0]+1.00)

#If it is a valid hour then we would add it with the required float minutes 
#{.:2f} is used to round the floating values with two decimal digits 
if((M[0]>=0 and M[0]<=23) and (M[1]>=0 and M[1]<=37)):
    print("{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}".format(k,k+0.04, k+0.09, k+0.15, k+0.19, k+0.22))

# for minutes between 38 and 59 
elif((M[0]>=0 and M[0]<=23) and (M[1]>=38 and M[1]<=59)):
    min = []  
    array = [M[1],M[1]+4, M[1]+9, M[1]+15, M[1]+19, M[1]+22]
    for i in array:
       if i< 60:
           min.append(M[0]+(i/100))
       else: 
           min.append(new+((i - 60)/100))
    for i in min:
        print("{:.2f}".format(i),end=' ')


else: 
    print("INVALID INPUT")

