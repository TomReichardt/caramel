from .tokens import Acronym, Word, Number, Other
from .token_container import TokenContainer

LEX_TOKENS = [Acronym, Word, Number, Other]


def get_remaining(index, data):
    if index >= len(data):
        return None
    else:
        return data[index:]


def lex_token(TokenClass, index, line):
    token = TokenClass.lex(line, index)
    if token:
        index += token.length
    return index, token


def get_next(index, data):
    line = get_remaining(index, data)
    if not line:
        return index, None

    for TokenClass in LEX_TOKENS:
        index, token = lex_token(TokenClass, index, line)
        if token:
            return index, token


def lexer(data):
    index = 0
    lexemes = []
    while True:
        index, lexeme = get_next(index, data)
        if not lexeme:
            break
        lexemes.append(lexeme)
    return TokenContainer(lexemes)
