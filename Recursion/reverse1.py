def reverse(iteratable):
    result = type(iteratable)()
    if iteratable == result: return result

    # the last element followed by the rest reversed
    return iteratable[-1:] + reverse(iteratable[:-1])

print reverse("hello")
print reverse([1, 2, 3, 4, 5])
