def validate_id(id_: int) -> int:
    if not isinstance(id_, int):
        raise TypeError("ID must be an integer.")
    elif id_ <= 0:
        raise ValueError("ID must be a positive integer.")
    return id_


def validate_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    elif not name.strip():
        raise ValueError("Name must be a non-empty string.")
    return name


def validate_price(price: int) -> int:
    if not isinstance(price, int):
        raise TypeError("Price must be an integer.")
    elif price <= 0:
        raise ValueError("Price must be a positive integer.")
    return price


def validate_quantity(quantity: int) -> int:
    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer.")
    elif quantity < 0:
        raise ValueError("Quantity must be a non-negative integer.")
    return quantity


def validate_integer_input(prompt: str, prompt_name: str) -> int:
    """Function to validate integer input from the user."""
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError(f"{prompt_name} must be an integer.")
