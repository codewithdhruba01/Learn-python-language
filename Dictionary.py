#Create a Dictionary
"""
info = {
    "Name":"Dhrubaraj", #ya sab key valu he
    "age": 22,
    "is_Adult": True
}
print(info)
"""

#nested Dictionary
#dictionary ke undar dict
"""
info={
    "name": "Dhrubaraj Pati",
     "subject" :{
    "Bengali": 29,
    "English": 54,
    "math": 59,
    "Bio": 79
}
}
print(info)
"""

#Update a Dictionary
"""
info = {
    "name":"Dhrubaraj",
     "age": 22,
    "is_Adult": True,
}

info["name"]= "Dhrubaraj Pati", #ya hoga update pati add hoga
info["surname"]= "Pati" #isme ak key valu add hoga Surname pati

print(info)
"""

#indivisual Subject print
"""
info={
    "name": "Dhrubaraj Pati",
    "subject" : {
      "Bengali": 29,
      "English": 54,
      "math": 59,
      "Bio": 79
}
}
print(info["subject"]) #isme keya huya ki info ke undar srip subject hi print huya

print(info["subject"]["Bio"]) #spacific ak ko bhi print kar sakta he ase
"""

"""
#Dictionary keys Methods
info={
    "name": "Dhrubaraj Pati",
    "subject" : {
      "Bengali": 29,
      "English": 54,
      "math": 59,
      "Bio": 79
}
}
print(info.keys()) #dict.keys() methods return all keys
"""

"""
#Dictionary values Methods
info={
    "name": "Dhrubaraj Pati",
    "subject" : {
      "Bengali": 29,
      "English": 54,
      "math": 59,
      "Bio": 79
}
}
print(info.values()) #dict.values() methods return all values
"""

"""
#Dictionary items Methods
info={
    "name": "Dhrubaraj Pati",
    "subject" : {
      "Bengali": 29,
      "English": 54,
      "math": 59,
      "Bio": 79
}
}
print(info.items()) #dict.items() methods return all (key values) pairs as tuples
"""

"""
#Dictionary .get Methods
info={
    "name": "Dhrubaraj Pati",
    "subject" : {
      "Bengali": 29,
      "English": 54,
      "math": 59,
      "Bio": 79
}
}
print(info.get("name")) #return the key according to value
"""


#Dictionary update Methods
info={
    "name": "Dhrubaraj Pati",
    "subject" : {
      "Bengali": 29,
      "English": 54,
      "math": 59,
      "Bio": 79
}
}
info.update({"city": "kolkata"}) #update new key value in Dictionary
print(info)


