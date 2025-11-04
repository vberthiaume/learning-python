# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
myDict = {
    "one" : 1,
    "two" : 2,
    3 : "three",                        # the type of the key and values doesn't need to be the same for all elements
    4.5 : ["four", "point", "five"]     # and values can even contain lists
    # ["four", "point", "five"] : 4     # but keys can't lol
}

# keys have to be strings or numbers, and have to be unique in the dictionary
print (myDict)

# dictionaries are accessed via keys
print (myDict["one"])

# you can also set dictionary data by creating a new key
myDict["seven"] = 7

# Trying to access a nonexistent key will produce an error
# print (myDict[asd])

# To avoid this, you can use the "in" operator to see if a key exists
print ("two" in myDict)

# You can retrieve all of the keys and values from a dictionary
print (myDict.keys())
print (myDict.values())

# You can also iterate over all the items in a dictionary
print ("====================================")
for key, val in myDict.items():
    print (key, val)