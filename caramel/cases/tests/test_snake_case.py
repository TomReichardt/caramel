from caramel import to_snake_case


def test_to_snake_case(string_permutations):
    for key, value in string_permutations.items():
        expected = string_permutations["snake"]
        output = to_snake_case(value)
        assert (
            output == expected
        ), f"""
        Failed to convert {key} case string, {value} to snake case
        Expected {expected}, got {output}
        """
