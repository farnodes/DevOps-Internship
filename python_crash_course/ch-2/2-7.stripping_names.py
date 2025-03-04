name_with_space = "\t rahul singh \n"
print("rahul singh chauhan:")
print(name_with_space)


# lstrip use
name = "    rahul singh"
print(name.lstrip())


text = "####python####"
print(text.lstrip("#"))

text = "abcabcRahulabc"
print(text.lstrip("abc"))


# rstrip use

name = "\tanuj rahulabcdef"
print(name.rstrip("def"))

name = "rahul chauhan------"
print(name.rstrip("-"))

# strip use 

office = "   farnodes company      "
print(office.strip())

office = "####farnode company####"
print(office.strip("#"))




word = "####hello words######"

print(word.lstrip("#"))
print(word.rstrip("#"))
print(word.strip("#"))