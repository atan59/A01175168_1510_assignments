"""Sort items in a list using selection sort algorithm."""
import doctest


def swap_elements(item_list: list, i: int) -> list:
    """
    Swap smaller elements with larger elements.

    :param item_list: a list
    :param i: an int
    :precondition: item_list must be a non-empty sortable list
    :precondition: i must be a positive integer
    :postcondition: Swap the lower element to the beginning
    :return: a list

    >>> swap_elements(['c', 'a', 'b'], 0)
    ['a', 'c', 'b']
    >>> swap_elements([4, 2, 7, 1], 0)
    [1, 4, 7, 2]
    >>> swap_elements([0.5, 1, 0, 4], 0)
    [0, 1, 0.5, 4]
    """
    for j in range(i + 1, len(item_list)):
        if item_list[i] > item_list[j]:
            item_list[i], item_list[j] = item_list[j], item_list[i]
    return item_list


def selection_sort(item_list: list) -> list:
    """
    Selection sort a list of items.

    :param item_list: a list
    :precondition: item_list must be a non-empty sortable list
    :postcondition: Sort item_list using selection sort algorithm
    :return: a list

    >>> selection_sort([3, 1, 5, 7, 2])
    [1, 2, 3, 5, 7]
    >>> selection_sort(['b', 'a', 'd', 'z', 'c'])
    ['a', 'b', 'c', 'd', 'z']
    >>> selection_sort([0.5, 0, 5, 2])
    [0, 0.5, 2, 5]
    """
    try:
        if not item_list:
            raise ValueError("Empty list is not a valid value.")
        for i in range(len(item_list) - 1):
            item_list = swap_elements(item_list, i)
    except (ValueError, TypeError) as e:
        print("Error: " + str(e))
    else:
        return item_list


if __name__ == "__main__":
    doctest.testmod()
