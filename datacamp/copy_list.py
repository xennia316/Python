# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
print(areas_copy)

# A change in areas does not affect areas_copy and vice versa because they do not point to thesame place in memory.
