# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#First your program must take the user input and convert it to a usable format.
#Next, you need to use it to update your nested list with an "x".

#column 2, row 3 would be entered as:
#23

#Write your code below this row 👇

column = int(position[0])
row = int(position[1])

map[row-1][column-1] = "X"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")