from .lexer import lexer
from .constructor import construct_snake_case, construct_camel_case


def to_snake_case(string):
    lexemes = lexer(string)
    return construct_snake_case(lexemes)


def to_camel_case(string):
    lexemes = lexer(string)
    return construct_camel_case(lexemes)
