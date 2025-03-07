"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
pattern = int(input("Enter Number of Rows:"))
for i in range (pattern):
    for j in range(0, i + 1):
        print(i, end=" ")
    print("\r")

"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
"""
row = int(input("Enter Reverse number of row:"))
for i in range (row, 0, -1):
    for j in range(0, i):
        print(i, end=' ')
    print("\r")

#Number triangle pattern
"""
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
"""
row = int(input("Enter a triangle number Row:"))
for i in range(1, row):
    cal = 1
    for j in range(row, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(cal, end=' ')
            cal += 1
    print("")