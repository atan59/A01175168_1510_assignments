"""Sort list to have red first, then white, and then blue."""


def dijkstra(colours_list: list):
    """
    Sort list to have red first, then white, and then blue.

    :param colours_list: a list
    :precondition: colours_list must be a non-empty list of strings
    :postcondition: Sort list to have red first, then white, and then blue.
    """
    try:
        if not colours_list:
            raise ValueError("This is not a valid value!")
    except (ValueError, TypeError) as e:
        print("Error: " + str(e))
    else:
        for i in range(len(colours_list)):
            if colours_list[i] == "red":
                colours_list.insert(0, colours_list.pop(i))
        for j in range(len(colours_list)):
            if colours_list[j] == "blue":
                colours_list.insert(len(colours_list) - 1, colours_list.pop(j))