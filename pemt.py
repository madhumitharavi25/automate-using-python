def matches(res):
	string = []
	#to remove duplicates
	for i in res:
	    if i not in string:
	        string.append(i)
	val = "-VS-"


	i = len(string)-1
	j = 1
	k = len(string)-1
	arr =[]

#finding two different teams
	while(i>=0):
		for j in range(0,k):
			if j >= len(string):
				break
			else:
				if i != j:
					new = (string[i] +val+ string[j]).split(' ')
					arr.append(new)
					j = j+1
		k =k-1
		i-=1

#string formatting
	d =(str(arr))
	e = (d.replace('[',''))
	f = (e.replace(']',''))
	g = (f.replace("'",""))


#printing the array
	final = g.split(',')
	print("TOTAL MATCHES:",len(final))
	for i in final:
		print(i)



res = []
team = ""
while ((team != 'q') or (team != 'Q')): #validating the input
    team = input()
    #print(string)
    if ((team == 'q')or (team == 'Q')):
        break
    else:
        res.append(team)
if (len(res)>=3 and len(res)<=12):#given input constraints
	matches(res)
else:
	quit()


		 
	

