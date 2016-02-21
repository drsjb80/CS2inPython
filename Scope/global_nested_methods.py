def outer():
    a = 0
    b = 1
    print (a)
    print (b)

    def inner():
        nonlocal b
        print (a)
        print (b)
        b = 4

    inner()

outer()
