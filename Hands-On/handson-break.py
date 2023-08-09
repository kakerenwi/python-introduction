# Where ever it is watermelon, make it into UPPERCASE and we don't need any further item

fruits = ["grapes", "kiwi", "watermelon", "banana", "mango", "oranges"]

for i in fruits:
    if i =="watermelon":
        print(i.upper()) # i is the placeholder for every item during the iteration. A String
        print("Found the fruit that we are looking for")
        break
    else:
        print(i)




