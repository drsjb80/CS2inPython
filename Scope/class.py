import sys

g = "global"

class enclosing:
    # this is an attribute, not a typical variable
    e = "enclosing"

    def local(self):
        l = "local"
        print "local:", sys._getframe().f_locals
        print "global:", sys._getframe().f_globals
        print "builtin:", sys._getframe().f_builtins


enclosing().local()
