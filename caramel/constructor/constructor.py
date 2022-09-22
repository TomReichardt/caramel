class Constructor:
    def __init__(self, tokens):
        self.tokens = tokens

    def remove(self, types=()):
        for token_type in types:
            for token in self.tokens.get_all_by_type(token_type):
                token.visible = False
        return self

    def set_body_lower(self, types=()):
        for token_type in types:
            for token in self.tokens.get_all_by_type(token_type):
                token.value = token.value.lower()
        return self

    def set_body_upper(self, types=()):
        for token_type in types:
            for token in self.tokens.get_all_by_type(token_type):
                token.value = token.value.upper()
        return self

    def set_body_title(self, types=()):
        for token_type in types:
            for token in self.tokens.get_all_by_type(token_type):
                token.value = token.value.title()
        return self

    def set_first_lower(self, types=()):
        if isinstance(self.tokens.first, types):
            self.tokens.first.value = self.tokens.first.value.lower()
        return self

    def set_rest_title(self, types=()):
        for t in self.tokens.rest:
            if types and not isinstance(t, types):
                continue
            t.value = t.value.title()
        return self

    def join_with(self, char="", types=()):
        if len(self.tokens.groups) > 1:
            for g in self.tokens.groups[1:]:
                g[0].value = char + g[0].value
        else:
            for t in self.tokens.rest:
                if types and not isinstance(t, types):
                    continue
                t.value = char + t.value
        return self

    def join_groups_with(self, char=""):
        if len(self.tokens.groups) > 1:
            for g in self.tokens.groups[1:]:
                g[0].value = char + g[0].value
        return self

    def join_tokens_with(self, char="", types=()):
        for t in self.tokens.rest:
            if types and not isinstance(t, types):
                continue
            t.value = char + t.value
        return self

    def remove_bookends(self):
        if self.tokens.bookends[0]:
            self.tokens.bookends[0].visible = False
        if self.tokens.bookends[1]:
            self.tokens.bookends[1].visible = False
        return self

    def construct(self):
        converted_tokens = self.tokens.body
        if self.tokens.bookends[0]:
            converted_tokens.insert(0, self.tokens.bookends[0])
        if self.tokens.bookends[1]:
            converted_tokens.append(self.tokens.bookends[1])

        return "".join([t.value for t in converted_tokens if t.visible])
