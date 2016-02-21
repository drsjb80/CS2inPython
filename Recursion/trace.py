from __future__ import print_function
import inspect

def print_stack():
    print ("---- TOS ----")
    for frame in inspect.getouterframes(inspect.currentframe())[2:]:
        print (frame[4])
    print ("---- BOS ----")

def foo ():
    print ("in foo")
    print_stack()

    def bar():
        print ("in bar")
        print_stack()

        def baz():
            print ("in baz")
            print_stack()

        baz()
        print ("after baz")
        print_stack()
    bar()
    print ("after bar")
    print_stack()

foo()
