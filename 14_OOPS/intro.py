# class Student:  # this is a Object
#     name = "Dhrubaraj"
#     age = 18
#
# s1 = Student() #this is a Class
# print(s1.name)
# print(s1.age)


#init function

class Student:
    name = "Dhrubaraj"
    def __init__(self): # ya jo constactor he ya apne ap call ho jata he
        print("this is a init function")

s1 = Student() #new object ko hi self bolte he