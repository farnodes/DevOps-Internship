name = ["mohit", "anuj", "rahul", "aakansh"]

name.append("swetank")
print("name append", name)


name.insert(1, "bttu")
print("insert name", name)

sorted_name = sorted(name)
print("sorted name", sorted_name)

name.sort(reverse=True)
print("reverse true", name)


print("number of len", len(name))


number = [11, 13, 17, 27, 99, 66]
sorted_num = sorted(number)
print("name of value minimum", sorted_num[0])
print("name of value maximum", sorted_num[-1])


