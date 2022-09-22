from .tokens import Word, Acronym, Number, Other


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
        self.first, self.rest = self.body[0], self.body[1:]
        self._create_groupings()

    def _create_groupings(self):
        self.groups = [[]]
        self.words, self.acronyms, self.numbers, self.others = [], [], [], []
        for token in self.body:
            getattr(self, f"{type(token).__name__.lower()}s").append(token)
            if type(token) in [Word, Acronym, Number]:
                self.groups[-1].append(token)
            elif type(token) is Other:
                self.groups.append([])

    def get_all_by_type(self, token_type):
        return getattr(self, f"{token_type.__name__.lower()}s")
