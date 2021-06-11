# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_heights = 0
for x in student_heights:
    sum_heights = int(sum_heights) + int(x)

average_height = int(sum_heights/len(student_heights))

print(f"The average height of student is \n{average_height}")


# student_heights = input("Please input student height separated by space. Eg. 157 189 128\n")
# student_height = student_heights.split(" ")
# sum_height = 0

# for sum_heights in student_height:
#     sum_height = int(sum_height) + int(sum_heights)

# average_height = int(sum_height/len(student_height))

# print(f"The average height of student is \n{average_height}")

