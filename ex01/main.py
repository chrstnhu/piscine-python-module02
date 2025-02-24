def what_are_the_vars(*args, **kwargs):
    """
    This function create an instance of ObjectC and pass
    the arguments to the ObjectC constructor to set attributes.
    """
    # Create an instance of ObjectC, passing all arguments
    obj = ObjectC()

    # Assign the positional arguments to the object with dynamic names
    for index, arg in enumerate(args):
        # Check if attribute 'var_{index}' exist
        if hasattr(obj, f"var_{index}"):
            return None
        setattr(obj, f"var_{index}", arg)
        
    # Assign the keyword arguments to the object
    for key, value in kwargs.items():
        # Check if attribute key exist
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)

    # Return the created object
    return obj


class ObjectC(object):
    def __init__(self, *args, **kwargs):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end\n")
        return
    
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end\n")


# Main
if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    # Output:
    # var_0: 7
    # end

    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    # Output:
    # var_0: None
    # var_1: []
    # end
    
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    # Output:
    # var_0: ft_lol
    # var_1: Hi
    # end

    obj = what_are_the_vars()
    doom_printer(obj)
    # Output:
    # end

    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    # Output:
    # a: 10
    # hello: world
    # var_0: 12
    # var_1: Yes
    # var_2: [0, 0, 0]
    # end

    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    # Output:
    # ERROR
    # end

    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
    # Output:
    # a: 10
    # var_0: 42
    # var_1: Yes
    # var_2: world
    # end