import re


def generator_numbers(text: str) -> [float]:
    """
    Generates floating point numbers from a given text.

    Args:
        text (str): The text to extract numbers from.

    Yields:
        float: Each floating point number found in the text.
    """
    letters = re.split(r" ", text)
    for element in letters:
        match = re.findall(r"\d+\.\d{2}", element)
        if any(match) and element == match[0]:
            yield float(element)


def sum_profit(text: str, generator_numbers: float) -> float:
    """
    Calculates the sum of profit using a generator function.

    Args:
        text (str): The text to extract numbers from.
        generator_numbers [float]: The generator function to use for extracting numbers.

    Returns:
        float: The total sum of profits.
    """
    total_inc = 0.00
    for number in generator_numbers(text):
        total_inc += number
    return total_inc



text1 = ("Загальний дохід працівника складається з декількох частин 1000.01 як основний дохід, доповнений додатковими "
"надходженнями 27.45 і 324.00 доларів.")
text2 = ("")
total_income = sum_profit(text1, generator_numbers)
print(f"Загальний дохід: {total_income}")
total_income = sum_profit(text2, generator_numbers)
print(f"Загальний дохід: {total_income}")