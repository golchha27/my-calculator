"""
Command Line Interface for Calculator.
Example usage: python src/cli.py add 5 3
"""

import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """
    CLI for basic calculator operations: add, subtract, multiply, divide,
    power, square_root (or sqrt). Handles errors gracefully.
    """
    try:
        if operation == "add":
            if num2 is None:
                raise click.ClickException("Missing second operand for addition")
            result = add(num1, num2)

        elif operation == "subtract":
            if num2 is None:
                raise click.ClickException("Missing second operand for subtraction")
            result = subtract(num1, num2)

        elif operation == "multiply":
            if num2 is None:
                raise click.ClickException("Missing second operand for multiplication")
            result = multiply(num1, num2)

        elif operation == "divide":
            if num2 is None:
                raise click.ClickException("Missing second operand for division")
            result = divide(num1, num2)

        elif operation == "power":
            if num2 is None:
                raise click.ClickException("Missing exponent for power operation")
            result = power(num1, num2)

        elif operation in ("sqrt", "square_root"):
            result = square_root(num1)

        else:
            raise click.ClickException(f"Unknown operation: {operation}")

        # Format result nicely: integer if whole number, else 2 decimals
        click.echo(int(result) if result == int(result) else f"{result:.2f}")

    except ZeroDivisionError:
        raise click.ClickException("Cannot divide by zero")

    except ValueError as err:
        raise click.ClickException(f"Error: {err}")
