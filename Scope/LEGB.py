from __future__ import print_function
import sys

g = "global"

def enclosing():
    e = "enclosing"

    def local():
        l = "local"
        e   # have to reference to make visible
        print ("local:", sys._getframe().f_locals)
        print ("global:", sys._getframe().f_globals)
        print ("builtin:", sys._getframe().f_builtins)

    local()

enclosing()
