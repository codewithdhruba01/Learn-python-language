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
# Pyramid of horizontal tables of number
"""
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100
"""
rows = 10
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()
