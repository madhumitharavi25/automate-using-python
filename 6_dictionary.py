cat = {'1': 'cat', '2':'dog','3':'goat'}
dog = {'1':'cat', '2':'ele','3':'hat'}
print(cat['2'])

# comparing 2 dictionaries
if cat==dog:
    print(1)
else:
    print(0)

#getting keys and values
print(cat.keys())
print(cat.values())

#assigning multiple values
for i, j in cat.items():
    print(i, j)

# to check the existance of the key
a = str(cat.get('5',0)) 
print(a)

# to add or set a value
cat.setdefault('4','fridge')
print(cat['4'])

 
  