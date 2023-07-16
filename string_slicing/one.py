# slice or indexing method for string
#  syntax : [start:stop:step]


name = "JOhn DOe"

fname = name[0:4] # [start:stop ]
lname = name[5:8] # [start:stop ]
crazy_name = name[0:8:2] # [start:stop:step ]
reverse_name = name [::-1] # [start:stop:step ] printing in reverse order

print(fname)
print(lname)
print(crazy_name)
print(reverse_name)


#slicing

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])