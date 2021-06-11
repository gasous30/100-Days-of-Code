#Write your code below this row 👇

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
#   `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

for x in range(1, 101):
    if(x % 3 == 0 and x % 5 == 0):
        print(f"FizzBuzz")
    elif(x % 3 == 0):
        print(f"Fizz")
    elif(x % 5 == 0):
        print(f"Buzz")
    else:
        print(x)
