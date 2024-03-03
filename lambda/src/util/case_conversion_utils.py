def convert_keys_to_snake_case(*, dict):
    """
    Converts the keys of the dictionary to snake_case.

    Parameters:
        dict (dict): The input dictionary.

    Returns:
        dict: The dictionary with keys converted to snake_case.
    """
    snake_case_dict = {}
    for key, value in dict.items():
        snake_case_key = camel_to_snake(key)
        if isinstance(value, dict):
            value = convert_keys_to_snake_case(value)
        snake_case_dict[snake_case_key] = value
    return snake_case_dict


def camel_to_snake(*, camel_case):
    """
    Converts a camelCase string to snake_case.

    Parameters:
        camel_case (str): The camelCase string.

    Returns:
        str: The snake_case string.
    """
    snake_case = ''
    for idx, char in enumerate(camel_case):
        if char.isupper() and idx > 0:
            snake_case += '_' + char.lower()
        else:
            snake_case += char.lower()
    return snake_case
