#String is data type that stores a Sequence of Characters
from operator import index

#Next line String
str = "Dhrubaraj\npati"
print(str)
print(len(str)) #Print Length

#Concatination String
#first Example
print("Hello" + "World") #this is a Concatination

#Second Example
str1 = "Hello" #Variable Store String data
str2 = "World"
print(str1+str2) #Concatination 2 String

#String Indexing
a = "Dhrubaraj" #0 1 2 3 4 5 6 7 8 - this is a index number. (always 0 Start index)
print(a[4])
#String me Space bhi count hota he

#capitalize Function
nam1= "Hello PYTHON" #Capitalize last Sentence
out = nam1.capitalize()
print(out) #Output - Hello python

#Replace Function
b = "I am Stadying Python"
print(b) #I am Stadying Python
print (b.replace("Python", "Java")) #I am Stadying Java

#Slicing
c = "Dhrubaraj Pati"
print(c[10:14])
print(c[5:])
print(c[:14])
