"""Generate a unique 6 digit lottery number."""
import random


def number_generator():
    """
    Generate a list of six unique numbers from 0 to 49.
    """
    result = random.sample(range(50), 6)
    result.sort()
    print("The lottery numbers are:", result)


"""
I used abstraction to ignore any details that would cause an error in the function and focused only on making it work. I
then used automation to organize the main function into well-defined steps.
"""
