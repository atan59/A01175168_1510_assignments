"""Generate a unique 6 digit lottery number."""
import random


def number_generator():
    """
    Generate a list of six unique numbers from 0 to 49.
    """
    result = random.sample(range(50), 6)
    result.sort()
    print("The lottery numbers are:", result)
