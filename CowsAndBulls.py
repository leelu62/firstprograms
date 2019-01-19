#simulate a game of cows and bulls
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
#For every digit that the user guessed correctly in the correct place, they have a “cow”. 
#For every digit the user guessed correctly in the wrong place is a “bull.” 
#Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
#Once the user guesses the correct number, the game is over. 
#Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random
number = random.randint(0,9999)

answer = str(number)

ans = list(answer)

print("Let's Play Cows & Bulls!")
play = input("Type Yes to play or No to quit:  ")

if play == "No":
	print("Exiting game...goodbye!")

else:
	count = 0
	cows = 0
	bulls = 0
		
	print("Great!\n.\n.\n.I am thinking of a four-digit number")
	print("\nFor every digit you guess in the correct place, you get a cow")
	print("\nFor every digit you get in the wrong place, you get a bull")
	print("\nI will let you know how many cows and bulls you have after each guess")
	print(".\n.\n.\n.\nOk here we go....")
	
	wrong = True
	
	while wrong: 
		guess = input("What is your guess?: ")
		guess = str(guess)
		
		check_guess = list(guess)
		for digit in check_guess:
			if digit in ans and check_guess.index(digit) == ans.index(digit):
				cows += 1
			if digit in ans and check_guess.index(digit) != ans.index(digit):
				bulls +=1
		
		count += 1	
		print("Cows: " + str(cows) + "\nBulls: " + str(bulls))
		wrong = True
		
		if cows == 4 and count == 1:
			print("You got it! Congratulations! It only took you 1 try!")
			break
		elif cows == 4 and count >1:
			print("You got it! Congratulations! It only took you " + str(count) + " tries!")
			break
		
		cows = 0
		bulls = 0
		
		
		
		
		
			
	
			
		
		
	
	


