programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

#Create an empty dictionary
# empty_dictionary = {}
# empty_dictionary["Loop"] = "The action of doing something over and over again."
# print(empty_dictionary)

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in the computer" 
# print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])