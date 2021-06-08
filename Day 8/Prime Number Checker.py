#Write your code below this line 👇

def prime_checker(number):
    div = 2
    while number % div != 0 and div < number:
        div += 1
    if(div == number):
        print(f"It's a prime number.")
    else:
        print(f"It's not a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



