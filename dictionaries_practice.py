# three major rivers dictionary

rivers = {"nile":"egypt","amazon":"brazil","thames":"london"}

for key, value in rivers.items():
	print("The " + key.title() + " runs through " + value.title() + ".")

for river in rivers.values():
	print(river.title())
	
for river in rivers:
	print(river.title())
	
	
	

