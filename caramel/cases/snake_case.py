from .utils import handle_bad_input
from ..constructor import Constructor
from ..lexer import lexer
from ..lexer.tokens import Acronym, Word, Other


def snake_case_constructor(tokens):
    return (
        Constructor(tokens)
        .remove(types=(Other,))
        .set_body_lower(types=(Word,))
        .join_tokens_with(char="_", types=(Acronym, Word))
        .construct()
    )


@handle_bad_input
def to_snake_case(data):
    tokens = lexer(data)
    return snake_case_constructor(tokens)
