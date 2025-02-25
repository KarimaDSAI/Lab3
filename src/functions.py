# src/functions.py

def sum_numbers(start: int, end: int) -> int:
    """
    Calculate the sum of numbers from start to end (inclusive).
    
    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.

    Returns:
        int: The sum of numbers from start to end.
    """
    total = 0
    for num in range(start, end):
        total += num
    return total
