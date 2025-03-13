f = open("demo.txt", "r") #Create a tex file mode is read
data = f.read() #txt file read
print(data) #print function
print(type(data)) # type of <class 'str'> String
f.close() #As a good practice to close the file.


f = open("demo.txt", "rb") # r  matlab read and b matlab binary do no ek seth bhi combine kar sakte
data = f.read()
print(data)
print(type(data))
f.close()


f = open("demo.txt", "r")
data = f.read(10) # particular 5 char he print karega
print(data)
f.close()