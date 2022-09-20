from .utils import handle_bad_input
from ..constructor import constructor
from ..constructor.rules import remove, all_upper, first_lower, body_title
from ..lexer import lexer
from ..lexer.tokens import Acronym, Word, Other


def camel_case_constructor(tokens):
    return constructor(
        rules=(
            remove(types=(Other,)),
            first_lower(types=(Word,)),
            body_title(types=(Word,)),
            all_upper(types=(Acronym,)),
        ),
        tokens=tokens,
    )


@handle_bad_input
def to_camel_case(string):
    tokens = lexer(string)
    return camel_case_constructor(tokens)
