import os

import send2trash
send2trash.send2trash()#sends to recycle bin

os.unlink("")#permanentely deletes file
os.rmdir()#deletes folder if no contents are there

import shutil
shutil.copy("sourcefolder","destinationfolder")#copies file
shutil.copytree("sourcefolder","destinationfolder")#copies folder
shutil.move("sourcefolder","destinationfolder")#moves the file
shutil.rmtree()#deletes folder even contents are there

import shelve
shelffile = shelve.open('mydata')#binary files
shelffile['cats'] =['1','2' ,'3','4']#acts as dictionary and stores 1,2,3,4 in cats
shelffile.close()

shelffile = shelve.open('mydata')
print(shelffile['cats'])#prints 1,2,3,4
print(shelffile.keys())
print(shelffile.values())


print(os.getcwd())#prints current directory
os.path.join("")#join the file path
os.chdir('')#change directory

#absolute file path will begin with root and relative donot
#relative file path starts with .\ 

os.path.abspath('files.py') #returns absolute file path
os.path.isabs("")# check whether it is absolute file path
os.path.relpath('',"") #returns relative file path
os.path.dirname()# returns file path
os.path.basename()# returns file name
os.path.exist()#checks if a file exists
os.path.isfile()#checks if a file exists
os.path.isdir()#checks if a file exists
os.path.getsize()#returns size of the file
os.listdir()# returns the names of the files
os.makedirs()#creats file 

hellofile = open("")#opens file
math = hellofile.read()
print(math)
hellofile.close()

hellofile.readlines() #reads file
hellofile.close()

hellofile = open("",'w') #overwrite the content
hellofile.write("hi how are you")
hellofile.close()

hellofile = open("",'a')# appends the text
hellofile.write("hi how are you")
hellofile.close()



