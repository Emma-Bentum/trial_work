'''This program invites friends for a dinner,

'''
#Inviting your friends for dinner together
#Using a list to take in people for the dinner
Guest_list = ['Elsie','Abena','Bensen','Eric']

#prints a welcome message for the invitees or guests.
print("Welcome Ladies and Gentle men,\n")

#Invites the guests individually
print(f'Hello, {Guest_list[0]}, i would love if we have dinner together.')
print(f'Hello, {Guest_list[1]}, i would love if we have dinner together.')
print(f'Hello, {Guest_list[2]}, i would love if we have dinner together.')
print(f'Hello, {Guest_list[3]}, i would love if we have dinner together.\n')

#One of the guests wouldn't be making it for the dinner, so we remove that person.
#So this code below does that.
unavailable_guest = Guest_list[0]
Guest_list.remove(unavailable_guest)

#Displays a message about the guest that won't be making it.
print(f"Alas, {unavailable_guest} can't make it for the dinner, ")

#Replacing the that won't be coming with a new guest.
#And printing a an informative message about the new guest. 
Guest_list[0] = "Thelma"
print(f"Henceforth, {Guest_list[0]}, {unavailable_guest}'s P.A will stand in place of her.\nthank you.\n")
'''print(f"{Guest_list}\n")'''

#Printing the second set of invitation message for each person.
#Initializing a variable i to 0.
i = 0
for index in Guest_list:
    print(f'Hello, {Guest_list[i]}, i would love if we have dinner together.')
    i += 1
    
'''print(f'Hello, {Guest_list[1]}, i would love if we have dinner together.')
print(f'Hello, {Guest_list[2]}, i would love if we have dinner together.\n')
'''
#Informing the guests about a new larger dinner table available.
print(f"\nHello everyone, I have found a bigger dinner table for us, let's add more guests!\n")

#Inserting a new guest at the first position of the lists of guests.
Guest_list.insert(0,'Samuel')

#Inserting another guest as the third person in the list.
Guest_list.insert(2,'Jeffery')

#Adding or appending a new guest to the end of the list.
Guest_list.append('Kofi')
print(f"{Guest_list}\n")


print('This is the final list for the dinner.\n')
print(f"{Guest_list}\n")

#Displays a message inviting all guests.
i = 0
for index in Guest_list:
    print(f"{Guest_list[i]}, i want to invite you for a dinner at DayAfterDay hotel.\n")
    i += 1

print("\nYou can invite only two people for dinner.\n")

#Using the "pop() method" to remove guests one at a time from the list.
##And leaving only two guests in the list.
'''The code beneath pops the last 4 guests invited for dinner in the Guest_list variable
and returns the first two Guests as the results.
'''
print("These are the people left for the dinner.")
i = 0

for index in range(4):
    Guest_list.pop()
print(Guest_list)

'''This code also pops or remove the first 4 Guests invited for dinner in the Guest_list variable.
   Starting with index 0
   i = 0

for index in range(4):
    Guest_list.pop(0)
print(Guest_list)

'''
#Printing the number of people invited for Dinner
print(f"\n I'm inviting only '{len(Guest_list)}' guests for the dinner tonight. ")

#Displaying the length of the last guest in the final list for the dinner.
print(len(Guest_list[-1]))

