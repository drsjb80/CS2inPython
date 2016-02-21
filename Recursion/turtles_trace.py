from __future__ import print_function
import inspect

def how_many_turtles (level):
    print ("---- TOS ----")
    for frame in inspect.getouterframes(inspect.currentframe())[1:]:
        print (frame[4])
    print ("---- BOS ----")

    if 1 >= level: return (4)
    return (how_many_turtles (level-1) * 4)

print (how_many_turtles (1))
print (how_many_turtles (2))
print (how_many_turtles (6))
