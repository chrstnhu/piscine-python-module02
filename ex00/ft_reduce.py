from collections.abc import Iterable

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.

    Args:
    - function_to_apply: a function taking an iterable.
    - iterable: an iterable object (list, tuple, iterator).
    
    Return:
    - A value, of same type of elements in the iterable parameter.
    - None if the iterable can not be used by the function.
    """
    
    # Check if the function is callable
    if not callable(function_to_apply):
        return None
    
    # Check if the iterable is an iterable object
    if not isinstance(iterable, Iterable):
        return None
    
    # Initialize the result
    iterable = iter(iterable)

    result = next(iterable)
    for element in iterable:
        result = function_to_apply(result, element)

    # Return an iterable
    return result


def add(x, y):
    return x + y

def multiply(x, y):
    return x * y


# Main
if __name__ == "__main__":

    test = [1, 2, 3, 4, 5]
    print("Original list:", test)

    print("\nTesting ft_reduce() with add() function:")
    result = ft_reduce(add, test)
    print(result) 

    print("\nTesting ft_reduce() with multiply() function:")
    result = ft_reduce(multiply, test)
    print(result, "\n")

    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print('Original list :', lst)

    # Subject test
    print("\nTesting main with lambda function:")
    x = [1, 2, 3, 4, 5]
    result = ft_reduce(lambda u, v: u + v, lst)
    print(result)
    # Output:
    # "Hello world"