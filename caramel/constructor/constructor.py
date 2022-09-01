def constructor(rules, tokens):
    for rule in rules:
        tokens = rule(tokens)

    body = "".join([t.value for t in tokens.body])
    bookends = [bookend.value if bookend else "" for bookend in tokens.bookends]
    return bookends[0] + body + bookends[1]
