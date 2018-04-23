def verify_int(arg):
    if type(arg) is not int:
        raise TypeError("Int expected")


def verify_positive(arg):
    if arg < 0:
        raise ValueError("Positive expected")


def verify_string(arg):
    if type(arg) is not str:
        raise TypeError("String expected")


def verify_string_and_value(arg, *args):
    verify_string(arg)
    if arg not in args:
        raise ValueError("Wrong value")
