# return wait time for a table depending on number of people
# in dinner party

print("Good Evening. Welcome to Talula's Garden.")
party_size = input("How large is your dinner party tonight?:\n")


if type(int(party_size)) == int:
	party_size = int(party_size)
	if party_size >= 1 and party_size <= 4:
		print("We can seat you right now, come this way please.")
	elif party_size > 4 and party_size <= 6:
		print("Your wait time will be about 10 - 15 minutes.")
	elif party_size >6:
		print("Your wait time may be close to half an hour.")
else:
	print("Get out of here you Buffoon!")

