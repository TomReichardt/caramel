class Acronym:
    def __init__(self, value, location):
        self.value = value
        self.length = len(value)
        self.location = location

    def __repr__(self):
        return f"Acronym: {self.value} - {self.location}"

    @classmethod
    def lex(cls, line, location):
        for idx, char in enumerate(line):
            if char.islower():
                idx -= 1
                break
            if not char.isupper():
                break
        else:
            idx += 1

        if idx >= 2:
            return cls(line[:idx], location)


class Word:
    def __init__(self, value, location):
        self.value = value
        self.length = len(value)
        self.location = location

    def __repr__(self):
        return f"Word: {self.value} - {self.location}"

    @classmethod
    def lex(cls, line, location):
        for idx, char in enumerate(line):
            if idx == 0 and not char.isalpha():
                break
            if idx > 0 and not char.islower():
                break
        else:
            idx += 1

        if idx:
            return cls(line[:idx], location)


class Number:
    def __init__(self, value, location):
        self.value = value
        self.length = len(value)
        self.location = location

    def __repr__(self):
        return f"Number: {self.value} - {self.location}"

    @classmethod
    def lex(cls, line, location):
        for idx, char in enumerate(line):
            if not char.isdigit():
                break
        else:
            idx += 1

        if idx:
            return cls(line[:idx], location)


class Other:
    def __init__(self, value, location):
        self.value = value
        self.length = len(value)
        self.location = location

    def __repr__(self):
        return f"Other: {self.value} - {self.location}"

    @classmethod
    def lex(cls, line, location):
        for idx, char in enumerate(line):
            if char.isalpha() or char.isdigit():
                break
        else:
            idx += 1

        if idx:
            return cls(line[:idx], location)
