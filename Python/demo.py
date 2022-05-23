# Variables (simple, complex)

## Simple Variables (integers, strings, Booleans [True/False])

    # i = 1
    # n = 3
    # z = i + n


# x = "Hello world!"


#print("The most common thing people do to demonstrate a language is:", x)

# something = True

# if something == True:
#     print("I did not know that")

## Complex variables (lists, dictionaries)

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# i = 1
# for item in planets:
#     print("In Star Trek, the planet", item, "would also be known as Sol", i)
#     i = i + 1 

### Dictionaries

captains = {'1701': 'Kirk',
            '1701-D': 'Picard', 
            '1864': 'Khan', 
            '75435': 'Janeway',
            '1031': 'Burnam'}

for ship in captains:
    print('The captain fo the NCC-'+ship, 'is', captains[ship])

    
