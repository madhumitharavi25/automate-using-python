
RS=['PANVEL', 'KHANDESHWAR', 'MANSAROVAR', 'KHARGHAR', 'BELAR', 'SEAWOOD', 'NERUL']
T = [0.00, 0.04, 0.05, 0.03, 0.04, 0.05, 0.03]
Trains = [7.30, 8.2, 12.45, 13.30, 14.44, 15.50, 9.15, 10.20, 23.59, 17.33, 19.20]
time_station = [0.00,0.04,0.09,0.12,0.16,0.21,0.24]


time = input("Enter current time(hour.min)float")
time = list(map(float,time.split('.')))
print(time)


print(RS)
print("At which station you are right now? Choose from above")
stationname = input()


station = stationname.upper()
if station.upper() in RS:
    station_number = RS.index(station)+1
else:
    print("INVALID INPUT")
    exit()

time_to_be_added = 0.0
for i in range(station_number):
    time_to_be_added += T[i]
    time += time_to_be_added
    
#print(time)

count=0
new_times = [x + round(time,2) for x in sorted(Trains)]
#print(new_times)
for i in new_times:
    if i > round(time):
        count+=1

print(count)