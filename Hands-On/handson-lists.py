# fruit1 = "kiwi"

# fruit2 = "grapes   "

# fruit3 = "apple"

# print(fruit1,fruit2,fruit3)

fruits =["kiwi", "grapes", "apple"]
students = ["naruto", "sasuke", "sakura"]
speeds = [30, 50, 20, 75, 100]
my_custom_list = ["vamsi", 28, 5.7, True, None]


print(fruits)
print(students)
print(speeds)
print(my_custom_list)

print(type(speeds))

print(len(fruits)) # length to count the items inside.
print(len(speeds))


fruits =["kiwi", "grapes", "apple"]

print(fruits[0]) # index or position
print(students[2]) # index for sakura
print(fruits[-1]) # this will give you the last item
input = len(fruits)
print(fruits[input-1])

print(type(input)) # this shows that the class is an interger.

#what if you want a subset of a list
students = ["samba", "jane", "samba", "ironman", "spiderman", "hulk"]

print(students[1:]) # prints a list of jane to hulk
print(students[1:4]) # This will print a list of jane to ironman
print(students[3:5]) # prints from ironman to spiderman

#To Modify jane to rachel
students[1] = "rachel"

print(students) # the new list showa jane has been replaced with rachel

students[2] = "captain america"

print(students) # samba has been replaced with captain america

students.reverse() # this reverses the order of nales listed on the list
print(students)

fruits = ["kiwi", "grapes", "apple", "orange", "banana", "strawberry", "watermelon", "pineapple", "mango", "pear", "cherry", "blueberry", "raspberry", "blackberry", "apricot", "plum", "peach", "nectarine", "pomegranate", "grapefruit", "lemon", "lime", "coconut", "fig", "guava", "passion fruit", "cantaloupe", "honeydew melon", "cucumber", "papaya", "kiwifruit", "persimmon", "cranberry", "avocado", "papaya", "dragon fruit", "date", "jackfruit", "kiwi berry", "lychee", "mangosteen", "persimmon", "quince", "rhubarb", "tangerine", "starfruit", "blackcurrant", "boysenberry", "elderberry", "gooseberry"]

# lets sort the list in alphabetical order.
fruits.sort()
print(fruits)

print(fruits.index("kiwi")) # the position of kiwi item
print(fruits[23])

fruits.remove("watermelon") # this removes watermelon from the list

fruits.append("soursop") # this adds soursop to the list.

fruits = ["avocado", "apricot", "apple", "grapes"]
# to access fruits individually we do 
fruits[0]
fruits[1]
fruits[2]
fruits[3]

for each_fruit in fruits:
    print(each_fruit) # to access every item one by one. Avoids writing many lines of code

fruits.clear() # clears the content from the list
print(fruits)

