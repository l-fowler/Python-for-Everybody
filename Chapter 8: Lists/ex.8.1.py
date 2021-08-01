"""
Exercise 1: Write a function called chop that takes a list and modifies it, removing
the first and last elements, and returns None. Then write a function called middle that
takes a list and returns a new list that contains all but the first and last elements.
"""

list = [1, 2, 3, 4, 5]

def chop(list):
    """
    Removes the first and last elements of a list, and returns None.
    Input: list = [1, 2, 3]
    Output: None
    """
    list2 = list[1:-1]
print(chop(list))   # Returns None

def middle(list):
    """
    Modifies a list and returns all but the first and last elements.
    Input: list = [1, 2, 3]
    Output: list without first and last elements, [2]
    """
    list2 = list[1:-1]
    return(list2)
print(middle(list)) # Returns [2, 3, 4]
