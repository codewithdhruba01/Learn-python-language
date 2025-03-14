with open ("demo.txt","r") as f:  #with syntax auto complite karta he huma alagse f.close karna nehi parta
    data = f.read()
    print(data)

#hum write bhi kar sakte
with open ("demo.txt","w") as f:
    data = f.write("add new data")


#Deleting a file
#using OS module

import os
os.remove("file_name") #jo bhi file tum delete karna chaho us file ka  nam likhna parega
