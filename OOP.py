# practice creating classes and methods

class FamilyMember():
	def get_full_name(self):
		print(self.firstname + " " + self.lastname)
	def get_birthday(self):
		print(self.birthday)

amon = FamilyMember()
amon.firstname = "Amon"
amon.lastname = "Greco"
amon.birthday = "October 3, 2016"

jenna = FamilyMember()
jenna.firstname = "Jenna"
jenna.lastname = "Shannon"
jenna.birthday = "June 2, 1985"

amon.get_full_name() 
amon.get_birthday()



