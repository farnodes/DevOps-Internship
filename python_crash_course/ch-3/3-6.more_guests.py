# Initial guest list
guests = ["Alice", "Bob", "Charlie"]

# Message about a bigger table
print("Great news! I found a bigger dinner table, so more guests can join us.")

# Adding new guests
guests.insert(0, "David")  # Adding to the beginning
guests.insert(len(guests) // 2, "Eve")  # Adding to the middle
guests.append("Frank")  # Adding to the end

# Sending new invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place. Looking forward to seeing you!")
