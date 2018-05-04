from collections import Iterable


def verify_types(*args):
    types = args

    def inner_function(func):
        def typeCheck(self, *args, **kwargs):
            if len(kwargs) > 0:
                args = list(kwargs.values())
            for idx, arg in enumerate(types):
                print(args[idx], type(args[idx]), types[idx])
                if type(args[idx]) is not types[idx] and\
                    not (isinstance(types[idx], Iterable) and
                        type(args[idx]) in types[idx]):
                    raise TypeError(
                        f'TypeError: Argument {idx + 1} of {func} is not {types[idx]}!'
                    )
            return func(self, *args)
        return typeCheck
    return inner_function


def verify_positive(func):
    def checkPositive(self, *args):
        for arg in args:
            if (type(arg) is float or
                    type(arg) is int) and arg < 0:
                raise ValueError("ValueError: Positive number requested!")
        return func(self, *args)
    return checkPositive



def verify_value(arg, *values):
    if arg in values:
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
