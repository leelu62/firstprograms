# draw a game board

size = input("What size game board would you like?\n")
size=int(size)

layer = 0


print("You have requested a " + str(size) + "x" + str(size) + " gameboard")


while layer < size:
	print(" --- " * size)
	print("|   |" * size)
	layer += 1
	
print(" --- " * size











