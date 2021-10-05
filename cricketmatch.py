def toString(List):
	return '-vs-'.join(List)

# Function to print permutations of string
# This function takes 	three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print(a)
        print(toString(a),end= " ")
        print("-vs-")
    else:
        for i in  range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function

string = []
team = ""
while ((team != 'q') or (team != 'Q')):
    team = input()
    #print(string)
    if ((team == 'q')or (team == 'Q')):
        break
    else:
        string.append(team)
n = len(string)
permute(string, 0, n-1)
        




