def makes10(a, b):
    """
    Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
    """
    return (a == 10 or b == 10) or (a + b == 10)

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))

# Alternative solution:
# return (a == 10 or b == 10 or a + b == 10)