from .utils import handle_bad_input
from ..constructor import Constructor
from ..lexer import lexer
from ..lexer.tokens import Acronym, Word, Other


def camel_case_constructor(tokens):
    return (
        Constructor(tokens)
        .remove(types=(Other,))
        .set_first_lower(types=(Word,))
        .set_rest_title(types=(Word,))
        .set_body_upper(types=(Acronym,))
        .construct()
    )


@handle_bad_input
def to_camel_case(string):
    tokens = lexer(string)
    return camel_case_constructor(tokens)
