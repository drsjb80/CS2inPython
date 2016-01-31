class dog:
    def say (self):
        return ("woof")

class cat:
    def say (self):
        return ("meow")

class bird:
    def say (self):
        return ("tweet")

class mouse:
    def say (self):
        return ("squeak")

class fox:
    def say (self):
        return ("Wa-pa-pa-pa-pa-pa-pow!")

animals = [dog(), cat(), bird(), mouse(), fox()]

for animal in animals:
    print (animal.say())
