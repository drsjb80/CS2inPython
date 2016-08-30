from __future__ import print_function
import inspect

def print_stack():
    print ("---- TOS ----")
    for frame in inspect.getouterframes(inspect.currentframe())[2:]:
        print (frame[4])
    print ("---- BOS ----")

def one():
    print ("in one")
    print_stack()

    def two():
        print ("in two")
        print_stack()

        def three():
            print ("in three")
            print_stack()

        three()
        print ("after three")
        print_stack()
    two()
    print ("after two")
    print_stack()

one()
