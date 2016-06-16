def reverse(a):
    result = type (a)()
    if a == result: return (result)

    # the last element followed by the rest reversed
    return (a[-1:] + reverse(a[:-1]))

print (reverse("hello"))
print (reverse([1, 2, 3, 4, 5]))
