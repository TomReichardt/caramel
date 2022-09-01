from .utils import handle_bad_input
from ..constructor import constructor
from ..constructor.rules import remove, all_lower, join_with
from ..lexer import lexer
from ..lexer.tokens import Acronym, Word, Other


def snake_case_constructor(tokens):
    return constructor(
        rules=(
            remove(types=(Other)),
            all_lower(types=(Word)),
            join_with(char="_", types=(Acronym, Word)),
        ),
        tokens=tokens,
    )


@handle_bad_input
def to_snake_case(data):
    tokens = lexer(data)
    return snake_case_constructor(tokens)
