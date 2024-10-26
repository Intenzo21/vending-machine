def validate_id(id_: int) -> int:
    if not isinstance(id_, int) or id_ <= 0:
        raise ValueError("ID must be a positive integer")
    return id_


def validate_name(name: str) -> str:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")
    return name


def validate_price(price: int) -> int:
    if not isinstance(price, int) or price <= 0:
        raise ValueError("Price must be a positive integer")
    return price


def validate_quantity(quantity: int) -> int:
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantity must be a non-negative integer")
    return quantity
