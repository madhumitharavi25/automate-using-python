import os

#prints all the files and folders
  for folder,subfolder,files in os.walk(""):
	print(folder)
	print(str(subfolder))
	print(str(files))
	print()
  

