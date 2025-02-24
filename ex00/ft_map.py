from collections.abc import Iterable

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.

    Args:
    - function_to_apply: a function taking an iterable.
    - iterable: an iterable object (list, tuple, iterator).
    
    Return:
    - An iterable.
    - None if the iterable can not be used by the function.
    """
    
    # Check if the function is callable
    if not callable(function_to_apply):
        return None
    
    # Check if the iterable is an iterable object
    if not isinstance(iterable, Iterable):
        return None
    
    # Return an iterable
    return (function_to_apply(element)  for element in iterable)


def double(x):
    return x * 2

def subtract(x):
    return x - 1

# Main
if __name__ == "__main__":

    print("Original list:")
    test = [1, 2, 3, 4, 5]
    for i in range(len(test)):
        print(test[i], end=", ")
    print()

    print("\nTesting ft_map() with double() function:")
    result = ft_map(double, test)
    print(list(result)) 

    print("\nTesting ft_map() with subtract() function:")
    result = ft_map(subtract, test)
    print(list(result))

    print("\nTesting ft_map() with a non-callable function:")
    result = ft_map(2, test)
    if result == None:
        print("None")
    else:
        print(list(result))

    print("\nTesting ft_map() with a non-callable iterable:")
    result = ft_map(double, 1)
    if result == None:
        print("None")
    else:
        print(result)