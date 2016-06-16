def reverse(iteratable):
    result = type(iteratable)()
    if iteratable == result: return result

    # the answer is the rest reversed followed by the first
    return reverse(iteratable[1:]) + iteratable[:1]

print reverse("hello")
print reverse([1, 2, 3, 4, 5])
