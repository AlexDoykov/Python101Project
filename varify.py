def varify_int(arg):
    if type(arg) is not int:
        raise TypeError("Int expected")


def varify_positive(arg):
    if arg < 0:
        raise ValueError("Positive expected")
