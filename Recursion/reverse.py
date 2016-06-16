def reverse(a):
    result = type (a)()
    if a == result: return (result)

    # the answer is the rest reversed followed by the first
    return reverse(a[1:]) + a[:1]

print (reverse("hello"))
print (reverse([1, 2, 3, 4, 5]))
