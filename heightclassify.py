N = int(input())
candidates = []
height = []


#getting the input for candidates and height

string = ''
while((string != 'q') or (string != 'Q')):
	string = input()
	if ((string == 'q') or (string == 'Q')):
		break
	else:
		candidates.append(string)

number = ""
while(number.isalpha() == False):
	number = input()
	#print(number.isalpha())
	if (number.isalpha()== True):
		break
	else:
		num = float(number)
		height.append(num)




if (len(candidates) == len(height)):
	result = dict(zip(candidates,height)) #converting the list of 
	                         #height and candidates to dictionary
	
	#sorting the height in the reverse order
	height.sort(reverse = True)
	new =  []
	for w in sorted(result, key=result.get, reverse=True):
		new.append(w) #matching the names with new height
	
	for i in range(0,N): # printing for the given range
		print(new[i])

else:
	quit()
