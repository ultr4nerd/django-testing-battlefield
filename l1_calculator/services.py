"""Calculator level app services"""

from typing import Optional, Union, Tuple

Number = Union[int, float]


def parse_number(number: Optional[str]) -> Optional[Number]:
    """Converts a string number into a real number"""
    try:
        return int(number)
    except (ValueError, TypeError):
        try:
            return float(number)
        except (ValueError, TypeError):
            return None


def parse_operator(operator: Optional[str]) -> Optional[str]:
    """Check if operator is valid and returns it, otherwise it returns None"""
    operators = ["+", "-", "*", "/", '**']
    if type(operator) != str:
        return None
    operator = operator.strip()
    if operator in operators:
        return operator
    else:
        return None


def parse_elements(
        first: Optional[str], operator: Optional[str], second: Optional[str]
) -> Tuple[Optional[Number], Optional[str], Optional[Number]]:
    """Parse every element, returning None for that element if is invalid"""
    first = parse_number(first)
    operator = parse_operator(operator)
    second = parse_number(second)
    return first, operator, second


def calculate(first: Optional[str], operator: Optional[str], second: Optional[str]) -> Optional[Number]:
    """Parse and calculate two numbers with the specified operator, returning None if something went wrong"""
    first, operator, second = parse_elements(first, operator, second)
    if None in (first, operator, second):
        return None
    else:
        if operator == "+":
            return first + second
        if operator == "-":
            return first - second
        if operator == "*":
            return first * second
        if operator == "/":
            return first / second if second != 0 else None
        if operator == "**":
            return first ** second
