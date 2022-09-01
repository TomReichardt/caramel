from .utils import handle_bad_input
from ..constructor import constructor
from ..constructor.rules import remove, all_upper, all_title
from ..lexer import lexer
from ..lexer.tokens import Acronym, Word, Other


def pascal_case_constructor(tokens):
    return constructor(
        rules=(
            remove(types=(Other)),
            all_title(types=(Word)),
            all_upper(types=(Acronym)),
        ),
        tokens=tokens,
    )


@handle_bad_input
def to_pascal_case(string):
    tokens = lexer(string)
    return pascal_case_constructor(tokens)
