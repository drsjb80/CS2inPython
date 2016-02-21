a = 0
print a

def foo():
    global a
    print a
    a = 4

foo()

print a
