#Practice Question 1

marks = {}
x = int(input("Bengali Marks : "))
marks.update({"Bengali": x})
x = int(input("English Marks : "))
marks.update({"English": x})
x = int(input("Math Marks : "))
marks.update({"Math": x})
x = int(input("Java Marks : "))
marks.update({"Java": x})
print(marks)