def reverse(a):
    result = type (a)()
    if a == result: return (result)

    result += reverse(a[1:]) + a[:1]

    return (result)

print (reverse("hello"))
print (reverse([1, 2, 3, 4, 5]))
