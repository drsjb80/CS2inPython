def reverse(iteratable):
    result = type(iteratable)()
    if iteratable == result: return result
    if 1 == len(iteratable): return iteratable

    return iteratable[-1:] + reverse(iteratable[1:-1]) + iteratable[:1]

print reverse("hello")
print reverse([1, 2, 3, 4, 5])
print reverse([[1, ["one", "two"], 2], [3, 4], 5])
