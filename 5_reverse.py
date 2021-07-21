num = int(input())
num1 = int(input())
sty = str(num)
get = list(sty)
reverse = ''
for i in range(len(get)-1,-1,-1):
    reverse+=get[i]
#print(str(reverse))
res=int(reverse)
#print(res)
#print(type(res))
if res > num1:
    print(res)
else:
    print(-1)


