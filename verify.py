def varify_int(arg):
    if type(arg) is not int:
        raise TypeError("Int expected")
    else:
        return True


def varify_positive(arg):
    if arg < 0:
        raise ValueError("Positive expected")
    else:
        return True


def verify_direction(direction):
    if direction == 'up' or direction == 'down' or direction == 'left' or direction == 'down':
        return True
    raise ValueError("Wrong direction")

