"""A tiny temperature conversion utility."""


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    print(f"98.6F is {fahrenheit_to_celsius(98.6):.1f}C")
    print(f"37C is {celsius_to_fahrenheit(37):.1f}F")
