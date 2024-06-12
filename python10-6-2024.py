# List items are ordered, changeable, and allow duplicate values.

#  list is changeable

# we can add or delete elements in the list 

# the elements in the list stored inside closed brackets

# we can find the length of the list using len function 

# we can find whether it is list or not by using type function 

# list  Allows duplicate elements 

qwerty1 = ["apple", "banana", "cherry"]
print(qwerty1[1])

# we can access any elements by using its position 

# we can use negative numbers by taking them as positon of list from end 

# we can do slicing in list 

qwerty2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(qwerty2[2:5])


# we can change the values in the list by using their positon values 

qwerty3 = ["apple", "banana", "cherry"]
qwerty3[1] = "blackcurrant"
print(qwerty3)


# we can the second and third value by using only one word

qwerty4 = ["apple", "banana", "cherry"]
qwerty4[1:3] = ["watermelon"]
print(qwerty4)



qwerty5 = ["apple", "banana", "cherry"]
qwerty6 = ("kiwi", "orange")
qwerty5.extend(qwerty6)
print(qwerty5)


qwerty7 = [100, 50, 65, 82, 23]
qwerty7.sort()
print(qwerty7)




# Tuples are used to store multiple items in a single variable.

#A tuple is a collection which is ordered and unchangeable.

#Tuple items are ordered, unchangeable, and allow duplicate values.

mytuple = ("apple", "banana", "cherry")

print(type(mytuple))


mytuple1 = ("apple", "banana", "cherry")

print(type(mytuple1))


#A set is a collection which is unordered, unchangeable*, and unindexed.


# Set items are unchangeable, but you can remove items and add new items.

#Set items are unordered, unchangeable, and do not allow duplicate values.


asd= {"apple", "banana", "cherry", True, 1, 2}

print(asd)


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)



thisset1 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset1.update(tropical)

print(thisset1)


#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


print(len(thisdict))


