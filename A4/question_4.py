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
