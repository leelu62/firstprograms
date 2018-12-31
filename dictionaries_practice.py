#People

people = []

person_0 = {"name":"Christopher Greco","age":"35","city":"Rockville Centre"}
person_1 = {"name":"Jenna","age":"33","city":"Oceanside"}

people = (person_0,person_1)

for person in people:
	print(person["name"] + " is " + person["age"] + " years old and "
			"lives in " + person["city"] + ".")
