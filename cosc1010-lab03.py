# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab 03 
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list


state = ["Wyoming", "Colorado", "Montana"]

#print the entire list

print(state)

#now print the first element in the list
print(state[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(state[2])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided

print(f"{state[1].upper()}is south of{state[0].upper()}")


print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
state.append("Washington")
state.append("Oregon")
state.append("California")

print(state)
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
state[4] = "Maine"
print(state)
#Insert the state Texas to be the third element in the list, again printing your list
state.insert(2,"Texas")
print(state)
#Using the `del` statement remove the fourth item from the list, print your list 
del state[3]
print(state)
#Remove Texas using its value, print the list
state.remove("Texas")
print(state)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(sorted(state))
print(state)
#Permanently sort your list in reverse order, printing it out
state.reverse()
print(state)
#Using the reverse method reverse the list and print it
state.reverse()
print(state)