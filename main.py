import logging
import sys

from src.vending_machine.machine import VendingMachine
from src.vending_machine.product import Product
from src.vending_machine.utils import validate_integer_input

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

MENU_STR = "\n1. Insert Money" \
           "\n2. Select Product" \
           "\n3. Display Products" \
           "\n4. Display Valid Denominations" \
           "\n5. Add New Product" \
           "\n6. Reload Product" \
           "\n7. Reload Currency" \
           "\n8. Exit\n"

PRODUCT_ID = "Product ID"


def insert_money(vending_machine: VendingMachine) -> None:
    """
    Insert money into the vending machine.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    try:
        denom = validate_integer_input("Enter denomination to insert (in pence): ", "Denomination")
        vending_machine.insert_money(denom)
        logger.info(f"Inserted money: {denom}p. Current balance: {vending_machine.balance}p.")
    except ValueError as e:
        logger.error(f"Error inserting money: {e}")


def select_product(vending_machine: VendingMachine) -> None:
    """
    Select a product to purchase from the vending machine.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    display_products(vending_machine)
    try:
        product_id = validate_integer_input("\nEnter product ID to purchase: ", PRODUCT_ID)
        vending_machine.purchase_product(product_id)
        logger.info(
            f"Product with ID {product_id} purchased successfully. Remaining balance: {vending_machine.balance}p.")
    except ValueError as e:
        logger.error(f"Error selecting product: {e}")


def display_products(vending_machine: VendingMachine) -> None:
    """
    Display the available products in the vending machine.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    logger.info("Displaying available products...")
    print("\nAvailable products:")
    for product_info in vending_machine.list_products():
        print(f"\t{product_info}")


def display_valid_denominations(vending_machine: VendingMachine) -> None:
    """
    Display the valid denominations accepted by the vending machine.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    logger.info("Displaying valid denominations...")
    print(f"\nValid denominations: {', '.join(f'{denom}p' for denom in vending_machine.get_valid_denominations())}")


def add_product(vending_machine: VendingMachine) -> None:
    """
    Add a new product to the vending machine.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    try:
        product_id = validate_integer_input("Enter product ID: ", PRODUCT_ID)
        product_name = input("Enter product name: ")
        product_price = validate_integer_input("Enter product price (in pence): ", "Product price")
        product_quantity = validate_integer_input("Enter product quantity: ", "Product quantity")
        new_product = Product(id_=product_id, name=product_name, price=product_price, quantity=product_quantity)
        vending_machine.add_product(new_product)
        display_products(vending_machine)
        logger.info(f"Product {product_name} (ID: {product_id}) added successfully.")
    except (TypeError, ValueError) as e:
        logger.error(f"Error creating product: {e}")


def reload_product(vending_machine: VendingMachine) -> None:
    """
    Reload a product in the vending machine.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    try:
        display_products(vending_machine)
        product_id = validate_integer_input("Enter product ID to reload: ", PRODUCT_ID)
        quantity = validate_integer_input("Enter product quantity: ", "Product quantity")
        vending_machine.reload_product(product_id, quantity)
        logger.info(f"Product with ID {product_id} reloaded with quantity {quantity}.")
        logger.info(f"Updated product details: {vending_machine.select_product(product_id)}")
    except ValueError as e:
        logger.error(f"Error reloading product: {e}")


def reload_currency(vending_machine: VendingMachine) -> None:
    """
    Reload currency denominations in the vending machine.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    try:
        logger.info(f"Current denomination counts: {vending_machine.get_denomination_counts()}")
        denom = validate_integer_input("Enter denomination to reload (in pence): ", "Denomination")
        count = validate_integer_input("Enter currency quantity: ", "Currency quantity")
        vending_machine.reload_currency(denom, count)
        logger.info(f"Reloaded currency: {count} of {denom}p denomination.")
        logger.info(f"New denomination counts: {vending_machine.get_denomination_counts()}")
    except (TypeError, ValueError) as e:
        logger.error(f"Error reloading currency: {e}")


def dispense_change(vending_machine: VendingMachine) -> None:
    """
    Dispense change to the user when exiting the vending machine.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    logger.info("Dispensing change...")
    try:
        change = vending_machine.dispense_change()
        logger.info(f"Change {change} dispensed successfully.")
    except ValueError as e:
        logger.error(f"Error dispensing change: {e}")


def exit_program(vending_machine: VendingMachine) -> None:
    """
    Exit the vending machine application.

    Args:
        vending_machine (VendingMachine): The vending machine object
    """
    dispense_change(vending_machine)
    logger.info(vending_machine)
    logger.info("Exiting the Vending Machine application.")
    print("\nThank you for using the Vending Machine. Goodbye!")


def display_menu():
    """Display the main menu options."""
    print(MENU_STR)


def main():
    """
    The main entry point for the Vending Machine application.

    Initializes the vending machine, loads sample products, and manages the main application loop
    where the user selects options from a menu.
    """

    print("\nWelcome to the Vending Machine!\n")
    logger.info("Starting the Vending Machine application.")
    vending_machine = VendingMachine()

    # Sample products to load
    sample_products = [
        Product(id_=1, name="Soda", price=120, quantity=10),
        Product(id_=2, name="Chips", price=80, quantity=5),
        Product(id_=3, name="Candy", price=100, quantity=8)
    ]

    # Load sample products into the vending machine
    vending_machine.add_products(sample_products)
    logger.info("Sample products loaded into the vending machine.")
    logger.info(vending_machine)
    display_products(vending_machine)

    # Dictionary mapping user choices to functions
    options = {
        '1': insert_money,
        '2': select_product,
        '3': display_products,
        '4': display_valid_denominations,
        '5': add_product,
        '6': reload_product,
        '7': reload_currency,
    }
    while True:
        display_menu()
        choice = input("Please choose an option: ")

        if choice in options:
            options[choice](vending_machine)
        elif choice == '8':
            exit_program(vending_machine)
            break
        else:
            logger.warning("Invalid choice entered. Please try again.")


if __name__ == "__main__":
    main()
