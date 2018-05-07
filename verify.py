from collections import Iterable


def verify_types(*args, **kwargs):
    types = kwargs

    for position, arg in enumerate(args):
        types[position] = arg

    def decorator(func):
        def typeCheck(self, *args, **kwargs):
            arguments = kwargs.copy()
            for position, arg in enumerate(args):
                arguments[position] = arg


            for arg in types.keys():
                if arg in arguments.keys() and\
                    type(arguments[arg]) != types[arg] and\
                    not(isinstance(types[arg], Iterable) and
                        type(arguments[arg]) in types[arg]):
                    raise TypeError(
                        f'TypeError: Argument {arg} of {func} is not {types[arg]}!'
                    )

            return func(self, *args, **kwargs)
        return typeCheck
    return decorator


def verify_positive(func):
    # def decorator(func):
    def checkPositive(self, *args, **kwargs):
        for arg in args:
            if (type(arg) is float or
                    type(arg) is int) and arg < 0:
                raise ValueError("ValueError: Positive number requested!")
        for arg in kwargs:
            if (type(arg) is float or
                    type(arg) is int) and arg < 0:
                raise ValueError("ValueError: Positive number requested!")
        return func(self, *args, **kwargs)
    return checkPositive
    # return decorator



def verify_value(arg, values):
    if arg not in values:
        raise ValueError(f"{values} expected")
    else:
        return True


def verify_direction(*args):
    def inner_func(func):
        def check_if_direction_is_valid(self, direction):
            for allowed_direction in args:
                if direction == allowed_direction:
                    return func(self, direction)
            raise ValueError("Wrong direction.")
        return check_if_direction_is_valid
    return inner_func
