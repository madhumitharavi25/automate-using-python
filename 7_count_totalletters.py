import pprint
message ='aaaaIt was a raniny day'
count = {}


#.upper converts string to upper
for i in message.upper():
    count.setdefault(i,0)
#updates the value for the key in the dictionary
    count[i] = count[i]+ 1


print(count)
# print in a nice way
pprint.pprint(count)
#formats the print
rjtext =pprint.pformat(count)
print(rjtext)

#print(count.values())
#print(count.keys())
#print(count.get('z',0))
