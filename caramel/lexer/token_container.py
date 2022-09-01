from .tokens import Other


def pop_bookends(tokens):
    begin, end = None, None
    if type(tokens[0]) is Other:
        begin = tokens.pop(0)
    if type(tokens[-1]) is Other:
        end = tokens.pop(-1)
    return (begin, end), tokens


class TokenContainer:
    def __init__(self, tokens):
        self.bookends, self.body = pop_bookends(tokens)
