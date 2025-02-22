#set is the collection of the unordered items.
"""
nums = {1,2,3,4,5,6} #this is a valid set
print(nums)
print(type(nums))
"""

"""
nums2 = {1,2,3,3,3,"dhruba","dhruba"} #Duplicate velu not allow
print(nums2)
"""

"""
nums = set() #called Empty set
print(type(nums))
"""
#set add method --- set.add(element)
#set element immutable.
#duplicate velu not allow.
"""
example=set() #emty set
example.add(34) #Add function matlab 34 velu set ke undar add ho geya
example.add(56) #Add function
example.add(56) #duplicate velu
print(example) #print function
"""
#remove methods in set-------
"""
fruits = {"apple", "banana", "cherry"} #multiple velu pass kiya tuple form me.
fruits.remove("banana") #remove methods.
print(fruits) #print function.
print(type(fruits)) #Which type (set).
"""

#add methods Set
"""
example={"akash", "samir", 34, "alock", 89} #multiple velu pass karna ke leya tuple ko leya
example.add(39) #add method
example.add("Ankush") #add methods
print(example) #print statement
print(type(example)) #type of Set
"""

#pop Method set
"""
example = {"red", "green", "blue", "white", "yellow"}
print(example.pop()) #rendam velu print hoke ayaga
"""
#Union Method set
"""
example1 = {1,2,3,4}
example2 = {3,4,5,6,7}
print(example1.union(example2))   #final velu in 2 set union repeated values not allow
"""
#Intersection Method set
"""
example1 = {1,2,3,4}
example2 = {3,4,5,6,7}
print(example1.intersection(example2))    #do velu ko dekhega pahela same/common velu ko print karega
"""