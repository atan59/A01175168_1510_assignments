"""Mix two primary colours to make one secondary colour."""


def colour_mixer():
    """
    Mix two primary colours to make one secondary colour.
    """
    colour_1 = (input("Enter one primary colour: ")).lower()

    if colour_1 != "red" or "yellow" or "blue":
        print("You have entered an invalid colour.")

    colour_2 = (input("Enter one primary colour: ")).lower()

    if colour_2 != "red" or "yellow" or "blue":
        print("You have entered an invalid colour.")

    elif colour_1 == colour_2:
        print("You have entered two of the same colour.")

    elif colour_1 == "red":
        if colour_2 == "yellow":
            print("You have created orange.")
        elif colour_2 == "blue":
            print("You have created purple.")
    elif colour_1 == "yellow":
        if colour_2 == "red":
            print("You have created orange.")
        elif colour_2 == "blue":
            print("You have created green.")
    elif colour_1 == "blue":
        if colour_2 == "red":
            print("You have created purple.")
        elif colour_2 == "yellow":
            print("You have created green.")
