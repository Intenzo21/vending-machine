# Vending Machine Application

## Overview

This Vending Machine application simulates a real-world vending machine, allowing users to insert money, select
products, and manage the inventory and currency. The application is designed with modular components to facilitate
testing and future enhancements.

## Features

- **Insert Money**: Insert money in various denominations.
- **Select Product**: Choose a product to purchase.
- **Display Products**: Show all available products in the vending machine.
- **Display Valid Denominations**: Show all valid currency denominations accepted by the machine.
- **Add New Product**: Add a new product to the vending machine inventory.
- **Reload Product**: Restock a specific product in the inventory.
- **Reload Currency**: Add more currency denominations (used for returning change) to the vending machine.
- **Dispense Change**: Dispense change based on the user's remaining balance.

## Technologies Used

- Python 3.x
- Logging for tracking application events
- Custom classes for managing products and vending machine functionality

## Installation

To run this application, ensure you have Python 3.x installed. You can download the latest version of Python from the
official website: [python.org](https://www.python.org/).

Follow these steps to install the application:

1. Clone the repository:

    ```sh
    git clone https://github.com/Intenzo21/vending-machine.git
    ```

2. Navigate to the project directory:
    ```sh
    cd vending-machine
    ```
3. Install the required dependencies:
    ```sh
    pip3 install -r requirements.txt
    ```

## Usage

Run the main script to start the vending machine simulation:

```sh
python3 main.py
```

## Project Structure

- `src/vending_machine/machine.py`: Contains the `VendingMachine` class which handles the core functionality.
- `src/vending_machine/product.py`: Contains the `Product` class representing individual products.
- `src/vending_machine/currency.py`: Contains the `Currency` class for handling currency operations.
- `src/vending_machine/inventory.py`: Contains the `Inventory` class for managing product inventory.
- `src/vending_machine/utils.py`: Contains utility functions such as `validate_integer_input`.
- `tests/test_product.py`: Contains unit tests for the `Product` class.
- `tests/test_currency.py`: Contains unit tests for the `Currency` class.
- `tests/test_inventory.py`: Contains unit tests for the `Inventory` class.
- `tests/test_machine.py`: Contains unit tests for the `VendingMachine` class.
- `main.py`: Entry point for the vending machine simulation.

## Running Tests

To run the tests, use the following command:

```sh
python3 -m unittest discover -s tests
```

## Future Enhancement Ideas

- **Graphical User Interface**: Implement a GUI for a more intuitive and engaging user experience.

- **Dynamic Currency Restocking**: Implementing a feature that allows currency restocking based on user input (e.g.,
  amount inserted) or the available amount in the vending machine's storage.

- **Custom Error Handling**: Developing custom exceptions to provide clearer, more specific error messages in place of
  built-in exceptions.

- **Profit Tracking System**: Introducing a robust profit tracking system to monitor financial performance over time.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or feedback, please contact [casp3rmail@gmail.com](mailto:casp3rmail@gmail.com).