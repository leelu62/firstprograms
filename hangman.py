#Hangman game simulation

import random

print("Welcome to Hangman!\n.\n.\n.\n.\n")
decision= input("Are you ready to play? Type y or n:\n")


if decision.lower() == "n":
	print("Exiting game... Goodbye!")
elif decision.lower() == "y":
	print("Excellent! Let's get started...")
else:
	print("I do not understand your entry. Try again soon!")
	

	
with open('sowpods.txt') as f:
	words = list(f)

word = print(random.choice(words).strip())
print(type(word))
word_string = str(word)
print(word_string)
print(type(word_string))

print("I'm thinking of a word with " + str(len(word_string)) + " letters")
print(" _ " * len(word_string))





