f = open("demo.txt", "r") #Create a tex file mode is read
data = f.read() #txt file read
print(data) #print function
print(type(data)) # type of <class 'str'> String
f.close() #As a good practice to close the file.