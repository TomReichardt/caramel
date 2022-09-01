from functools import wraps


def handle_bad_input(func):
    @wraps(func)
    def wrapper(string):
        if (string is None) or (string == ""):
            return ""
        if string and not isinstance(string, str):
            return string
        return func(string)

    return wrapper
