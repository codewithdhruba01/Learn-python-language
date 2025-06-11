#wap to check if a singal character is a vowel or not
ch = input ("Enter a Singal Character: ")
if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(ch,"is a vowel")
else:
    print(ch," is not a vowel")

#WAP to check if the 3rd last character of a string is a vowel or not

str1 = input("Enter a string: ")
if len(str1)<= 2:
    print("given the word is too small")
else:
    ch = str1[-3]
    if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
        print(ch, "is a vowel")
    else:
        print(ch, "is not a vowel")
