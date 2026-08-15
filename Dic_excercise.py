
#NOTE: YOU CAN NEST DICTIONARIES INSIDE LISTS, LISTS INSIDE DICTIONARIES, AND EVEN DICTIONARIES INSIDE OTHER DICTIONARIES.
#the dictionary alien_0 stores the alien's color and points value.
alien_0 = {
    'color': 'green', 
    'points': '5'
    }

#Accessing and printing values in a Dictionary
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0["points"]
print(f"You have earned {new_points} points.")

# ADDING NEW KEY-VALUE PAIR AND DISPLAYING THE RESULTS.
alien_0['food'] = 'fried rice'
print(alien_0['food'])

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)



##Another way of accessing values in a dictionary without assigning a variable to the dictionary.
if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
    #Where {'foo': 1, 'bar': 2, 'baz': 3} is the dictionary and ['baz'] is the key been used to access the value.
    print({'foo': 1, 'bar': 2, 'baz': 3}['bar'])
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)

#MODIFYING VALUES IN A DICTIONARY
#Old dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

#New dictionary
alien_0['color'] = 'yellow'
alien_0['x_position'] = '25 NE',

print(f"The alien is now {alien_0['color']}")
print(alien_0)



##Tracking the position of the an alien that can move at different speeds.
'alien_current_speed = 25'
alien_1 = {'x_position': '0', 'y_position': '25', 'speed': 'medium'}
print(f"Original position: {alien_1['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
# The new position is the old position plus the increment
alien_1['x_position'] = str(x_increment)
print(f"The new position is: {alien_1['x_position']}")


## USING GET() TO ACCESS VALUES.
"""
For dictionaries, specifically, you can use the get() method to 
set a default value that will be returned if the requested key doesn’t exist.

The get() method requires a 'KEY' as a first argument. As a second 
optional argument, you can pass the value to be returned if the key doesn’t 
exist.

If you leave out the second argument in the call to get() and the key doesn’t exist, 
Python will return the value None
"""

alien_0 = {'color': 'green', 'speed': 'slow'}

# The get() function or method takes exactly one argument, but can take a second argument
# The default value to be displayed for the key 'points' is ('No point value assigned').
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)



#6-1. PERSON:
kenneth_details = {
    "first_name": 'Kenneth',
    "last_name": 'Anim',
    "age": '22',
    "city": 'Accra',
    "favorite_food": 'Gob3',
    "course": 'materials Engineering'
    }
print("\nThese are the pieces of information about my friend!.")

# The code below (the for loop), prints only the KEYS of kenneth_details.

print("\nPrinting the keys in kenneth_details")
for kenneth_detail in kenneth_details:
    print(f"{kenneth_detail}")

 
### 
### Intentionally left blank. 
### The code below (the for loop), prints only the values of the KEYS in kenneth_details.
print("\nPrinting the VALUES of the keys in kenneth_details!: \n")
for kenneth_detail in kenneth_details:
    print(f"{kenneth_details[kenneth_detail]}")
 

   
#6-2. FAVORITE NUMBERS:
favorite_numbers = {
    "kojo": '10' ,
    "kobina": '9',
    "kweku": '8',
    "Yaw": '7',
    "kofi": '6'
    } 


# The print function displays the KEYS with their respective VALUES without the curly braces.
# 
for favorite_number in favorite_numbers:
    # {favorite_numbers[favorite_number]} displays only the "values" of the various keys.
    # the {favorite_number} in the print function displays only the "keys" in the dictionary.
    print(f"\n{favorite_number}: {favorite_numbers[favorite_number]}")

# 6-3. Glossary:
programming_words = {
    "print":
        '\tDisplay a result', 
    "pop": 
        '\tremoves the last item from the dictionary.',
    "append": 
        '\tdds items to the end of the list',
    "del": 
        '\tDeletes the entire elements or items from the list,making it empty.',
    ".title()": 
        '\tCapitalize every starting letter of a word.',
    "get()": 
        '\tReturns the value of the argument, and if there is no argument, it displays an optional message '
    }

for programming_word, meaning in programming_words.items():
    break;

print(f"\n{programming_words['pop']}: {programming_words[programming_word]}")


## Looping through all the KEY-VALUE pairs
user_0 = {
    "username": 'efermi',
    "first_name": 'enrico',
    "last": 'fermi'
}

for k, v in user_0.items():
    print(f"\nkey: {k}")
    print(f"\nvalue: {v}")
    


