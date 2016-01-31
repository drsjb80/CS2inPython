class replicate:
    def readAndWrite (self):
        me = open (__file__, "r")
        newMe = open ("new" + __file__, "w")

        for line in me:
            newMe.write (line)
        me.close()
        newMe.close()

replicate().readAndWrite()
