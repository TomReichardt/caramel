from ..lexer.tokens import Acronym, Word, Number, Other


def pop_bookends(lexemes):
    begin, end = None, None
    if type(lexemes[0]) is Other:
        begin = lexemes.pop(0)
    if type(lexemes[-1]) is Other:
        end = lexemes.pop(-1)
    return begin, lexemes, end
