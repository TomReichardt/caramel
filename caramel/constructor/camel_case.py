from .utils import pop_bookends
from ..lexer.tokens import Acronym, Word, Number, Other


def construct_camel_case(lexemes):
    begin, lexemes, end = pop_bookends(lexemes)

    first = lexemes[0]
    body = first.value.upper() if type(first) is Acronym else first.value.lower()
    for lexeme in lexemes[1:]:
        if type(lexeme) is Other:
            continue
        elif type(lexeme) is Acronym:
            body += lexeme.value.upper()
        else:
            body += lexeme.value.title()
    return begin.value + body + end.value
