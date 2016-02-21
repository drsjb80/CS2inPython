def outer():
    a = 0
    b = 1

    def inner():
        nonlocal b
        print (a)
        print (b)
        b = 4

    inner()
    print (b)

outer()
