usernames_pw = {"jshann":"Noma!003","cgreco":"BabyAmon1228",
				"A$":"oldmcdonald"}

print("Welcome to the Grecopia System!")
print(".\n.\n.\n.")
username= input("Please enter your username:\n")

if username.lower() in usernames_pw:
	password = input("Please enter your password:\n")
	if password == usernames_pw[username]:
		print("Access Granted. Have a good session " + username +".")
	else:
		print("Access Denied")
else:
	print("Unknown username")
