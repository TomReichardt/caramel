from caramel import to_pascal_case


def test_to_pascal_case(string_permutations):
    for key, value in string_permutations.items():
        expected = string_permutations["pascal"]
        output = to_pascal_case(value)
        assert (
            output == expected
        ), f"""
        Failed to convert {key} case string, {value} to pascal case
        Expected {expected}, got {output}
        """
