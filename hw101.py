import random
print(dir(random))
n=input("Press Y to roll again and N to exit ") 
n="y"
while n== "y":
    no = random.randint(1,6)
    if no ==1:
        print("The number on the dice is one")
    if no ==2:
        print("The number on the dice is two")
    if no ==3:
        print("The number on the dice is three")
    if no ==4:
        print("The number on the dice is four")
    if no ==5:
        print("The number on the dice is five")
    if no ==6:
        print("The number on the dice is six")
    