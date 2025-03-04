bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[3])
print(bicycles[-2])


# Using Individual Values from a List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
messsage = f"my first bicycle was a {bicycles[2].title()}"
print(messsage)



# Modifying Elements in a List

name = ["shiv", "shivam", "ram", "ravi"]
name[0] = "rahul"
print(name)



# Appending Elements to the End of a List

name = ["ram", "mohan", "shubham", "anuj"]
name.append("rahul")
print(name)

number = [1, 2, 3, 4, 5]
number.append("7")
print(number)


# empty list, add the elements

motorcycle = []
motorcycle.append("honda")
motorcycle.append("yamha")
motorcycle.append("suzuki")
print(motorcycle)


# Inserting Elements into a List

name = ["ravi", "shiv", "rajesh", "pinku"]
name.insert(1, "rahul")
print(name)


number = [21, 22, 23, 24, 25]
number.insert(0, 1)
print(number)



# Removing Elements from a List

name = ["ravi", "shiv", "rajesh", "pinku"]
del name[1]
print(name)


number = [11, 12, 13, 14, 15]
del number[0]
print(number)

#Removing an Item Using the pop() Method
name = ["ravi", "shiv", "rajesh", "pinku"]
popped_name = name.pop()
print(popped_name)


number = [21, 22, 23, 34, 35]
remove_number = number.pop()
print(remove_number)



# Popping Items from Any Position in a List

name = ["ravi", "shiv", "rajesh", "pinku"]
pop_name = name.pop(0)
print(f"this is super mind {pop_name.title()}")



name = ["ravi", "shiv", "rajesh", "pinku", "anuj"]
master_mind = name.pop()
print(f"DevOps mind super {master_mind.title()}")



# Removing an Item by Value

name = ["ravi", "shiv", "rajesh", "pinku", "anuj"]
name.remove("anuj")
print(name)



number = [1, 2, 3, 4, 5]
number.remove(1)
print(number)

# print a reason for removing it from the list:

employe  = ["ravi", "shiv", "rajesh", "pinku", "anuj"]
expensive_emp = "ravi"
employe.remove(expensive_emp)
print(f"\n\t{expensive_emp.title()}  is more expensive employee")