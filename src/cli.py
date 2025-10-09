"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI with proper error handling."""
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
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except ZeroDivisionError:
        raise click.ClickException("Cannot divide by zero")

    except ValueError as e:
        raise click.ClickException(f"Error: {e}")

    except Exception as e:
        raise click.ClickException(f"Unexpected error: {e}")


if __name__ == "__main__":
    calculate()
