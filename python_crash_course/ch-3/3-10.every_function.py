name = ["rohan", "pooja", "shivam", "mohan", "ram", "anuj"]

print("print list", name)

name.append("ram")
print("After append :", name)

name.insert(1, "rahul")
print("name insert :", name)

name.remove("shivam")
print("name remove :", name)

popped_name = name.pop()
print("popped_name", popped_name)
print("after poping", name)


print("temporarily sorted list", sorted(name))



name = ["anuj", "rahul", "vikram",  "Amit"]
sorted_names = sorted(name) # Ascending order (छोटे से बड़े)
print("sorted_name", sorted_names)

number = [11, 12, 14, 28, 77, 20, 10]
sorted_number = sorted(number)
print("manimum number", sorted_number[0])
print("maximum number", sorted_number[-1])

name.sort(reverse=True) # Descending order
print("sorted in reverse list", name)

number = [21, 22, 23, 24, 25, 26]
number_sort = number.sort(reverse=True)
print("number reverse", number)

# print("max", number_sort[-1])
# print("min", number_sort[0])



name = ["anuj", "rahul", "vikram", "Amit"]

name.sort(reverse=True)
print("sort Reverse True", name)

print("lenth of name :", len(name))
name = ["anuj", "rahul", "vikram", "Amit"]
print("print lenth of list", len(name))

text = "hello world"
print("name of text", len(text))

del name[0]
print("after delte", name)


