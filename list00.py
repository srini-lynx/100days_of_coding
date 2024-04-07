#!/usr/bin/python

print("****************************************************************************************")
print("                          LIST      DATATYPE     EXAMPLES                               ")
print("****************************************************************************************")

Fruits = [ "orange", "papaya", "bannana", "grapes" ]

print(f"The Contents of Fruits List are :: {Fruits}")
print("We can modify the Contents of Lists, fruits First letter can be Upper case")

Fruits[0] = "Orange"
Fruits[1] = "Papaya"
Fruits[2] = "Bannana"
Fruits[3] = "Grapes"

print(f"Now after modifying the Fruits list Contents are ::  {Fruits}")
print("Appending 'Pineapple' to Fruits List")
Fruits.append("Pineapple")
print(f"After appending Pineapple, List contents are :: {Fruits}")

Veggies = [ "Tomato", "Carrot", "Potato", "Beans"]

print(f"Veggies List has :: {Veggies}")

print("Extending the Fruits List to Contain Veggies")

Fruits.extend(Veggies)

print(f"After Extending Fruits List Contents :: {Fruits}")

print("Insert  'Melon' into the Fruits list ")

Fruits.insert(4,"Melon")

print(f"After Inserting 'Melon' into Fruits List, Contents are :: {Fruits}")

print("Remove 'Melon' from the list")

Fruits.remove("Melon")

print(f"After Removing the 'Melon' from the Fruits list :: {Fruits}")
print(f"Lenght of List  :: {len(Fruits)}")

print(f"Count the Occurences of 'Orange' in the List :: {Fruits.count('Orange')}")


print(f"Bannana is at the Index :: {Fruits.index('Bannana')}")

Fruits.sort()
print(f"Sort the Fruit list :: {Fruits}")

Fruits.reverse()
print(f"After Reversing the Fruit list :: {Fruits}")
print("****************************************************************************************")
print("****************************************************************************************")
