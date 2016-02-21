def how_many_turtles (level):
    if 1 == level: return (4)
    return (how_many_turtles (level-1) * 4)

print (how_many_turtles (1))
print (how_many_turtles (2))
print (how_many_turtles (100))
