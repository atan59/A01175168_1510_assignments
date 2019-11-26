"""Sort items in a list using selection sort algorithm."""


def swap_elements(item_list: list, i: int) -> list:
    for j in range(i + 1, len(item_list)):
        if item_list[i] > item_list[j]:
            item_list[i], item_list[j] = item_list[j], item_list[i]
    return item_list


def selection_sort(item_list: list) -> list:
    try:
        if not item_list:
            raise ValueError("Empty list is not a valid value.")
        for i in range(len(item_list) - 1):
            item_list = swap_elements(item_list, i)
    except (ValueError, TypeError) as e:
        print("Error: " + str(e))
    else:
        return item_list
