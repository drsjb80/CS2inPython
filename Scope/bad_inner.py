def outer():
    a = 0
    b = 1

    def inner():
        print (a)
        print (b)
        b = 4

    inner()

outer()
