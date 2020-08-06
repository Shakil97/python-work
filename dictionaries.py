#dictionaries
my_stuff = {"key1" : 123, "key2":"value2","key3":{"123":[1,2,3]}}
print(my_stuff['key3']["123"][2].upper())

###
my_stuff2 = {"lunch":"pizza","bfast":"burger"}
my_stuff2["lunch"] = 'pasta'
my_stuff2["dinner"] = "beef"
print(my_stuff2["lunch"])
print(my_stuff2)