#Breakk - Used to terminate the loop When encountered.
#A break statement is used inside both the while and for loops.
#It terminates the loop immediately and transfers execution to the new statement after the loop.


#Continue - terminates execution in the current & Continues execution of the loop
#The continue statement causes the loop to skip its current execution at some point and move on to the next iteration.
#Instead of terminating the loop like a break statement, it moves on to the subsequent execution.

#Break Keyword Example ---
count = 0
while count <= 100:
    print (count)
    count += 1
    if count == 10: #jab count ka velu 9 hoga tab statement break karega
        break #Break ke bad kuch bhi check nehi hoga

#Continue Keyword Example ---
for i in range(0, 5): #'0' se start hoga '5' par stop hoga
    if i == 3: #Jab 'i' ka velu 3 hoga tab continue keyword Skip karega
        continue #Skip
    print(i)

