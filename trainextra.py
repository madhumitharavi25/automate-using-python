
M = input("Enter current time(hour.min)float")
k = float(M)
M = list(map(int,M.split('.')))
if (M[0] > 23 or M[1]>59):  #validating the time(24-hours format)
    print("INVALID INPUT")
    exit()
else:
    new = (M[0]+1.00)


RS=['PANVEL', 'KHANDESHWAR', 'MANSAROVAR', 'KHARGHAR', 'BELAPUR', 'SEAWOOD', 'NERUL']
print(RS)
print("At which station you are right now? Choose from above")
stationname = input()
station = stationname.upper()
if station.upper() in RS: #checking for station index
    station_number = RS.index(station)+1
else:
    print("INVALID INPUT")
    exit()


#If it is a valid hour then we would add it with the required float minutes 
min = []
if((M[0]>=0 and M[0]<=23) and (M[1]>=0 and M[1]<=35)):
    min = [k,k+00.04, k+00.09, k+00.12, k+00.16, k+00.21, k+00.24]

# for minutes between 38 and 59 
elif((M[0]>=0 and M[0]<=23) and (M[1]>=36 and M[1]<=59)):
        min = []
        arr = []
        array = [M[1],M[1]+4, M[1]+9, M[1]+15, M[1]+19, M[1]+21,M[1]+24]
        for i in array:
            if i< 60:
                min.append(M[0]+(i/100))
            else: 
              min.append(new+((i - 60)/100))
        for i in min:
            arr.append("{:.2f}".format(i))#storing with two decimal values
        #print(min)

else: 
    print("INVALID INPUT")


#function to find trains which are yet to arrive for the current day at the station
def total_number(j):
    count = 0
    for i in range(0,station_number):
        if j > min[i]:
            count = count + 1
        final = 0
        if count == station_number:
            final = final +1
    return final


Trains = [7.30, 8.2, 12.45, 13.30, 14.44, 15.50, 9.15, 10.20, 23.59, 17.33, 19.20]
result = list(map(total_number,Trains))
no_of_trains = 0
for i in result:  #counting the number of trains
    if i == 1:
        no_of_trains = no_of_trains +1
print(no_of_trains)
