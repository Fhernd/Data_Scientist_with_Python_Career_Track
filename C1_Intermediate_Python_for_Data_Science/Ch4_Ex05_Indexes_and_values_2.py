# Exercise:

# Indexes and values (2)

# For non-programmer folks, room 0: 11.25 is strange. Wouldn't it be better if the count started at 1?


# Instructions:

# Adapt the print() function in the for loop on the right so that the first printout becomes "room 1: 11.25", the
# second one "room 2: 18.0" and so on.


# Code:

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas):
    print('room {}: {}'.format(index + 1, area))


