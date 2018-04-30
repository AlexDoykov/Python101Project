def verify_int(arg):
    if type(arg) is not int:
        raise TypeError("Int expected")
    else:
        return True


def verify_positive(arg):
    if arg < 0:
        raise ValueError("Positive expected")
    else:
        return True


def verify_string(arg):
    if type(arg) is not str:
        raise TypeError("String expected")
    else:
        return True


def verify_float(arg):
    if type(arg) is not float:
        raise TypeError("Float expected")
    else:
        return True


def verify_number(arg):
    if type(arg) is not int and type(arg) is not float:
        raise TypeError("Int or float expected")
    else:
        return True


def verify_class_type(arg, class_type):
    if type(arg) is not class_type:
        raise TypeError(f"{class_type} expected")
    else:
        return True


def verify_value(arg, *values):
    if arg in values:
        raise ValueError(f"{values} expected")
    else:
        return True


def verify_direction(*args):
    def inner_func(func):
        def check_if_direction_is_valid(self, direction):
            for index, allowed_direction in enumerate(args):
                if direction == allowed_direction:
                    return func(self, direction)
            raise ValueError("Wrong direction.")
        return check_if_direction_is_valid
    return inner_func
