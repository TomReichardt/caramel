from .utils import handle_bad_input
from ..constructor import Constructor
from ..lexer import lexer
from ..lexer.tokens import Acronym, Word, Other


def pascal_case_constructor(tokens):
    return (
        Constructor(tokens)
        .remove(types=(Other,))
        .set_body_title(types=(Word,))
        .set_body_upper(types=(Acronym,))
        .construct()
    )


@handle_bad_input
def to_pascal_case(string):
    tokens = lexer(string)
    return pascal_case_constructor(tokens)
