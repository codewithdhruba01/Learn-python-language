#Simple half pyramid Star pattern
# *
# * *
# * * *
# * * * *
# * * * * *
Star = int(input("Enter Number of Rows:"))
for i in range(0, Star):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")


# * * * * *
# * * * *
# * * *
# * *
# *
Star = int(input("Enter Number of Rows:"))
for i in range (Star + 1, 0, -1):
    for j in range (0, i-1):
        print("*", end=' ')
    print(" ")


#Equilateral triangle
   #       *
   #      * *
   #     * * *
   #    * * * *
   #   * * * * *
   #  * * * * * *
   # * * * * * * *
star = int(input("Enter Equilateral triangle Number of Row:")) #size of the triangle
for i in range(1, star + 1):
    # Print spaces
    for j in range(star - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # Move to the next line



# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
star = int(input("Enter Row Number:"))
for i in range(1, star+1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(star - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
row = int(input("Enter a row number:")) # Number of rows for the upper half

# Upper half of the pattern
for i in range(1, row + 1):
    # Print spaces
    for j in range(row - i):
        print(" ", end=" ")
    # Print stars
    for k in range(i):
        print("*", end=" ")
    print()

# Lower half of the pattern
for i in range(row - 1, 0, -1):
    # Print spaces
    for j in range(row - i):
        print(" ", end=" ")
    # Print stars
    for k in range(i):
        print("*", end=" ")
    print()
#Diamond-shaped pattern of stars
# Prints the upper half with increasing stars and decreasing spaces.
# Prints the lower half with decreasing stars and increasing spaces.
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

rows = int(input("Enter Row of Diamond-shaped Number:"))
# Upper half of the diamond
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()
