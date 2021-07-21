import copy
cat = [1,2,3,4,1]
a = cat.index(1)
#gives the index value
print(a)
#except index other methods does not work for 
#combination of strings and integer
#string doesnot have append method 
cat.append(5)
b = cat
print(b)
cat.insert(1,7)
c = cat
print(c)
#remove the first value
cat.remove(1)
d = cat
print(d)
#deletes the value in index 0
del cat[0]
e = cat
print(e)
#prints in asec order
cat.sort()
f = cat 
print(f) 
#prints in reverse order
cat.sort(reverse = True)
g = cat
print(g)
print(cat)
cat = ['A','a','s','S']
#In sorting uppercase comes first before lowercase
cat.sort()
print(cat)
#the below code helps to sort both 
#the upper and lower case combined
cat.sort(key=str.lower)
print(cat)
#doesnot modify the cat list
cheese = copy.deepcopy(cat)
cheese[1] = 42
print(cheese)
print(cat)
#\ denotes indentation and we can 
# continue typing in the second line
print('....... end  ' + \
        '.......')


