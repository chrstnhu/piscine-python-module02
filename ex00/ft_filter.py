from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.

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
    return (element for element in iterable if function_to_apply(element))


def inferiorToTen(x):
    return x < 10

def superiorToTen(x):
    return x > 10

def egalToTen(x):
    return x == 10


# Main
if __name__ == "__main__":

    print("Original list:")
    test = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
    print(test)

    print("\nTesting ft_filter() with inferiorToTen() function:")
    result = ft_filter(inferiorToTen, test)
    print(list(result)) 

    print("\nTesting ft_filter() with superiorToTen() function:")
    result = ft_filter(superiorToTen, test)
    print(list(result))

    print("\nTesting ft_filter() with egalToTen() function:")
    result = ft_filter(egalToTen, test)
    print(list(result))

    print("\nTesting main with lambda function:")
    x = [1, 2, 3, 4, 5]

    # Subject test
    result = ft_filter(lambda dum: not (dum % 2), x)
    print(result)
    # Output:
    # <generator object ft_filter at 0x7f709c777d00> # The adress will be different

    result = list(ft_filter(lambda dum: not (dum % 2), x))
    print(list(result))
    # Output:
    # [2, 4]