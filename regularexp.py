import re
name = re.compile(r'<(.*?)>')
print(name.findall("first: <Madhu>"))
only = re.compile(r'<(.*)>')
print(only.findall("<Madhu> hi how are you.>"))

line = re.compile(r'.*')
print(line.search("Madhu. \nhi how are you."))


fullline = re.compile(r'.*', re.DOTALL)
print(fullline.search("Madhu. \nhi how are you."))

vowelregex = re.compile(r'[a,e,i,o,u]',re.I)
print(vowelregex.findall("Madhu I am Here!!"))



#find and replace
namesregex = re.compile(r'Agent \w+')
print(namesregex.sub("redacyed","Agent Madhu gave to Agent Alice"))

names1regex = re.compile(r'Agent (\w)\w*')
print(names1regex.sub(r"Agent \1*****","Agent Madhu gave to Agent Alice"))




#used for multi-line and to add comments so to 
# improve readability

re.compile(r''' 
	\d\d\d   #area code  
	-        
	\d\d\d   #first 3 digits
	-
	\d\d\d''',re.VERBOSE)



re.compile(r''' 
	\d\d\d   #area code  
	-        
	\d\d\d   #first 3 digits
	-
	\d\d\d''',re.I| re.DOTALL|re.VERBOSE)

