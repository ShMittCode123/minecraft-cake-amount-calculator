# MCCakeMaker starting
print("MCCakeMaker is starting...")
print("Please enter your resources")

#Amount of eggs, milk, wheat, and sugar and assigning variables
eggsMin = 1
eggsAmount = int(input("Enter amount of eggs: "))
print("You have", eggsAmount, "eggs")
milkMin =  2
milkAmount = int(input("Enter amount of milk: "))
print("You have", milkAmount, "buckets of milk")
wheatMin = 3
wheatAmount = int(input("Enter amount of wheat: "))
print("You have", wheatAmount, "wheat")
sugarMin = 3
sugarAmount = int(input("Enter amount of sugar: "))
print("You have", sugarAmount, "sugar")

#extra variables
cake = eggsMin + milkMin + wheatMin + sugarMin
tCake = eggsAmount + wheatAmount + milkAmount + sugarAmount

#main code
if cake == tCake:
    print("1 cake will be made")
elif tCake > cake:
	print(tCake / cake, " cakes will be made")
else:
	print("No cakes today :(")

#close program
print("MCCakeMaker is shutting down...")
