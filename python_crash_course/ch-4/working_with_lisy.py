# A Closer Look at Looping ??
# Looping Through an Entire List

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)


# Doing More Work Within a for Loop

magicians = ["alice", "david", "corolina"]

for magician in magicians:
    print(f"magician name {magician.title()} for best magicians")


# Add a second line to our message for new line

names = ["mohit", "anuj", "aakansh", "swetank"]

for name in names:
    print(f"all of employe {name.title()}, software engineer")
    print(f"all employee multiple type {name.title()} engineer \n")
print("Thank you, everyone")  # Doing something After a for loop


# forgetting to indent Additional lines

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick{magician.title()} \n")

message = "Hello Python world!"
print(message)


