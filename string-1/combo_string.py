def combo_string(a, b):
    """
    Given 2 strings, a and b, return a string of the form short+long+short, 
    with the shorter string on the outside and the longer string on the inside. 
    The strings will not be the same length, but they may be empty (length 0).
    """
    if len(a) > len(b):
        return b + a + b
    return a + b + a

print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))