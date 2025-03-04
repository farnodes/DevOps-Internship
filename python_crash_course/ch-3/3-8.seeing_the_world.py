places = ["Tokyo", "Santorini", "Machu Picchu", "Paris", "New York"]

print("original order:", places)

print("Alphabetically Sorted List:", sorted(places))

print("list is still in its original order:", places)

print("Reverse-Alphabetically Sorted List:", sorted(places, reverse=True))

print("List After sorted(places reverse=True):", places)

places.reverse()
print("List After reverse():", places)

places.reverse()
print("List After reverse() again:", places)


places.sort()
print("List After sort():", places)

 
places.sort(reverse=True)
print("List After sort(reverse=True):", places)

