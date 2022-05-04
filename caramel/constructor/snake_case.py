from .utils import pop_bookends
from ..lexer.tokens import Acronym, Word, Number, Other


def construct_snake_case(lexemes):
    begin, lexemes, end = pop_bookends(lexemes)

    body = lexemes[0].value.lower()
    for lexeme in lexemes[1:]:
        if type(lexeme) is Other:
            continue
        elif type(lexeme) is Number:
            body += lexeme.value
        else:
            body += "_" + lexeme.value.lower()
    return begin.value + body + end.value
