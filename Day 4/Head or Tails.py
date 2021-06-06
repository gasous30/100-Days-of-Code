import random

# 0 = Tails
# 1 = Heads

random = random.randint(0,1)
if(random == 0):
    x = 'Tails'
else:
    x = 'Head'
print(x)