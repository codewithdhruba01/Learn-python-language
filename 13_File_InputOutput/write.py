# "W" --- Write
# "a" --- Append
#file ko create bhi kar sakte
f = open("write.txt","w") #append ke undar bhi khol sakte
f.close()


f = open("demo2.txt", "w")
f.write("Writing to a File") #hum is ke undar kuch bhi likh ke overwrite kar sakte
#jo bhi likhe ga o sab demo.txt ke undar stor hoga
f.close()

#hum purano deta ke undar, neya deta add bhi kar sakte append karke
f = open("demo2.txt", "a") #append kiya
f.write("Today learn about file system") #same line pe add hoke ayega
f.close()

#Next line pe append karne ke liya
f = open("demo2.txt", "a") #append kiya
f.write("\nToday learn about javascript") #ya next line pe append hoke ayaga
f.close()

#r+ mode pe file ko over write kar sakte
f = open("write.txt", "r+")
f.write("abcs") #This overwrite/change hoke sample replace hoga
f.close()