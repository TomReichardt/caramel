from caramel import to_camel_case


def test_to_camel_case(string_permutations):
    for key, value in string_permutations.items():
        expected = string_permutations["camel"]
        output = to_camel_case(value)
        assert (
            output == expected
        ), f"""
        Failed to convert {key} case string, {value} to camel case
        Expected {expected}, got {output}
        """
