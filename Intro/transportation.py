class wheel:
    def __init__ (self, diameter):
        self.diameter = diameter

    def getDiameter (self):
        return (self.diameter)

class vehicle:
    def __init__ (self, numWheels, diameter):
        self.wheels = [wheel (diameter) for _ in range (numWheels)]

    def __str__ (self):
        return ("number of wheels: " + str (len (self.wheels)) + \
            ", diameter: " + str (self.wheels[0].getDiameter()))

# new style
# class car (vehicle, object):
#     def __init__ (self, diameter):
#         super (car, self).__init__ (4, diameter)

# old style
class car (vehicle):
    def __init__ (self, diameter):
        vehicle.__init__ (self, 4, diameter)

    def __str__ (self):
        return ("I'm a car, " + vehicle.__str__ (self))

class bicycle (vehicle):
    def __init__ (self, diameter):
        vehicle.__init__ (self, 2, diameter)

    def __str__ (self):
        return ("I'm a bicycle, " + vehicle.__str__ (self))

print (vehicle (6, 24))
print (car (18))
print (bicycle (29))
