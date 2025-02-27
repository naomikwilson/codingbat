def missing_char(str, n):
    """
    Given a non-empty string and an int n, return a new string where the char at index n has been removed.
    The values of n will be a valid index of a char in the original string (i.e. n will be in the range 0 to len(str) -1 inclusive).
    """
    return (str[:n] + str[n + 1:])
    
print(missing_char("kitten", 1))
print(missing_char("kitten", 0))
print(missing_char("kitten", 4))

# Alternative solution:
#   front = str[:n]
#   back = str[n+1:]
#   return front + back