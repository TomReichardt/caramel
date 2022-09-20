def constructor(rules, tokens):
    for rule in rules:
        tokens = rule(tokens)

    converted_tokens = tokens.body
    if tokens.bookends[0]:
        converted_tokens.insert(0, tokens.bookends[0])
    if tokens.bookends[1]:
        converted_tokens.append(tokens.bookends[1])

    return "".join([t.value for t in converted_tokens if t.visible])
