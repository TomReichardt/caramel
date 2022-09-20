def remove(types=()):
    def _remove(tokens):
        for token_type in types:
            for token in tokens.get_all_by_type(token_type):
                token.visible = False
        return tokens

    return _remove


def all_lower(types=()):
    def _all_lower(tokens):
        for token_type in types:
            for token in tokens.get_all_by_type(token_type):
                token.value = token.value.lower()
        return tokens

    return _all_lower


def all_upper(types=()):
    def _all_upper(tokens):
        for token_type in types:
            for token in tokens.get_all_by_type(token_type):
                token.value = token.value.upper()
        return tokens

    return _all_upper


def all_title(types=()):
    def _all_title(tokens):
        for token_type in types:
            for token in tokens.get_all_by_type(token_type):
                token.value = token.value.title()
        return tokens

    return _all_title


def first_lower(types=()):
    def _first_lower(tokens):
        if isinstance(tokens.first, types):
            tokens.first.value = tokens.first.value.lower()
        return tokens

    return _first_lower


def body_title(types=()):
    def _body_title(tokens):
        for t in tokens.body[1:]:
            if types and not isinstance(t, types):
                continue
            t.value = t.value.title()
        return tokens

    return _body_title


def join_with(char="", types=()):
    def _join_with(tokens):
        if len(tokens.groups) > 1:
            for g in tokens.groups[1:]:
                g[0].value = char + g[0].value
        else:
            for t in tokens.body[1:]:
                if types and not isinstance(t, types):
                    continue
                t.value = char + t.value
        return tokens

    return _join_with


def join_groups_with(char=""):
    def _join_groups_with(tokens):
        if len(tokens.groups) > 1:
            for g in tokens.groups[1:]:
                g[0].value = char + g[0].value
        return tokens

    return _join_groups_with


def join_tokens_with(char="", types=()):
    def _join_tokens_with(tokens):
        for t in tokens.body[1:]:
            if types and not isinstance(t, types):
                continue
            t.value = char + t.value
        return tokens

    return _join_tokens_with


def remove_bookends(tokens):
    if tokens.bookends[0]:
        tokens.bookends[0].visible = False
    if tokens.bookends[1]:
        tokens.bookends[1].visible = False
    return tokens
