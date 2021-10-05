spam  = 'hello World'
a = spam.upper()
b = a.lower()
print(a,b) 
#to check the string character
print(spam.islower())
print(spam.isupper())
print(spam.isdecimal())
print(spam.isalpha())
print(spam[5].isspace())
print(spam.title())
print(spam.startswith('h'))
print(spam.endswith('d'))

#string to list
c = ['cats','dogs','bats']
d = '  '.join(c)
print(d) 

#list to string
print(spam.split())
print(spam.split('m'))

#string justification
print(spam.rjust(20))
print(spam.ljust(20,'-'))
print(spam.center(20,'*'))

#string seperation
print(spam.strip())
name = "madhumitha   "
print(name.lstrip())

#replace and formating string
print(spam.replace('e','i'))
print('hello %s Iam %s' %(a,name))
    