
i =1
string = []
N = int(input()) #number of people allowed for registration 

if ((N >=1) and (N<=10)): #given input constraints for number of people
	while(i<=N):
		a = int(input()) 
		if ((a>=10) and (a <= 100)): #given input constraints for age
			string.append(a)
		else:
			print("INVALID INPUT")		
		i =i+1
else:
	print("INVALID INPUT")


if (len(string) > 0):
	new = []
	arr = []
	for i in string:
		if ((i >=60) and (i <= 100)): # seperating senior citizen
			new.append(i)

	#alloting the second row 		
	if len(new) >= 5:
		for i in range(0,5):
			arr.append(new[i])
			string.remove(new[i])
	elif len(new) <= 5:
		for i in range(0,len(new)):
			arr.append(new[i])
			string.remove(new[i])
	#print(string)

	#printing the time in minutes
	print("QUEUE1 TIME: "+str(len(string)*15)+"mins")
	print("QUEUE2 TIME: "+str(len(arr)*15)+"mins")



