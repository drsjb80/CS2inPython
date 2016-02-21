from __future__ import print_function

def how_many_turtles (level):
    if 1 == level: return (4)
    hmt = how_many_turtles (level-1)
   return (hmt * 4)

print (how_many_turtles (1))
print (how_many_turtles (2))
print (how_many_turtles (10))
