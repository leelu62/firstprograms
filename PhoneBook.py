#practice using object-oriented programming
#encapsulating data

class Phonebook():
	
	def __init__(self):
		self.__entries = {}
	
	def add(self, name, phone_number):
		self.__entries[name] = phone_number
		
	def get_entry(self, name):
		if name in self.__entries:
			return self.__entries[name]
	
	def __len__(self):
		return len(self.__entries)
	
		
book = Phonebook()
book.add("Greco","516-225-9067")
book.add("Shannon","516-536-9255")
book.add("Marmo","516-225-9036")


choice = input("Welcome to the Phone Book.\n.\n.\n.\n.\nWould you like to"
		" enter a new entry or find a record? Enter 1 to enter"
		" a new entry or 2 to find a record:\n")

if choice == "1":
	entry = input("Please enter the name and separated by commas:\n")
	splitted_entry = entry.split()
	new_name = splitted_entry[0]
	new_number = splitted_entry[1]
	book.add(new_name, new_number)
	print(book.get_entry(new_name))

elif choice == "2":
	record = input("Please enter the name you would like to look up:\n")
	print(book.get_entry(record))


else:
	print("Invalid entry")

	


