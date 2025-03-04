name = ["mohit", "anuj", "aakansh", "swetank", "rahul"]

sorted_name = sorted(name)

print("maximum big alphabet", sorted_name[-1])
print("minimum small alphabet", sorted_name[0])


number = [21, 22, 23, 24, 25, 26]
number_sort = number.sort(reverse=True)
print("number reverse", number)



number = [21, 22, 23, 24, 25]

sorted_num = sorted(number)

print("maximum big alphabet", sorted_num[-1])
print("minimum small alphabet", sorted_num[0])




numbers = [11, 13, 17, 27, 99, 66]

min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        min_num = num

print("min number", min_num)
print("max_number", max_num)



numbers = [11, 13, 17, 27, 99, 66]

min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:  
        min_num = num
    if num > max_num:  
        max_num = num

print("Minimum value:", min_num)
print("Maximum value:", max_num)
