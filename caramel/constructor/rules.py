def remove(types=()):
    def _remove(tokens):
        tokens.body = [t for t in tokens.body if not isinstance(t, types)]
        return tokens

    return _remove


def all_lower(types=()):
    def _all_lower(tokens):
        for t in tokens.body:
            if types and not isinstance(t, types):
                continue
            t.value = t.value.lower()
        return tokens

    return _all_lower


def all_upper(types=()):
    def _all_upper(tokens):
        for t in tokens.body:
            if types and not isinstance(t, types):
                continue
            t.value = t.value.upper()
        return tokens

    return _all_upper


def all_title(types=()):
    def _all_title(tokens):
        for t in tokens.body:
            if types and not isinstance(t, types):
                continue
            t.value = t.value.title()
        return tokens

    return _all_title


def first_lower(types=()):
    def _first_lower(tokens):
        if types and isinstance(tokens.body[0], types):
            tokens.body[0].value = tokens.body[0].value.lower()
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
        for t in tokens.body[1:]:
            if types and not isinstance(t, types):
                continue
            t.value = char + t.value
        return tokens

    return _join_with


def remove_bookends(tokens):
    tokens.bookends = ["", ""]
    return tokens
