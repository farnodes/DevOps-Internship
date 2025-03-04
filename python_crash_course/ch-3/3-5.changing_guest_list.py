# guests = ["anuj", "ravi", "swetank"]

# for guest in guests:
#     print(f"most gest {guest} welcome to every person")

guests = ["anuj", "ravi", "swetank"]

not_invite = "ravi"
print(f"not invite this function {not_invite} next function invite ")

new_guest = "mohit"
guests[guests.index(not_invite)] = new_guest

print("\nnew invition")
for guest in guests:
    print(f"welcome {guest} invation for you")
