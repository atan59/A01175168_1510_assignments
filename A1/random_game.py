"""Short module with functions to play Rock, Paper, Scissors."""
import random
import doctest


def computer_choice_convert(choice):
    """
    Convert int choice to string choice.

    :param choice: an int
    :precondition: choice must be an int
    :postcondition: Convert int to a string choice
    :return: a string
    >>> computer_choice_convert(0)
    'rock'
    >>> computer_choice_convert(1)
    'paper'
    >>> computer_choice_convert(2)
    'scissors'
    """
    if choice == 0:
        convert = "rock"
    elif choice == 1:
        convert = "paper"
    elif choice == 2:
        convert = "scissors"
    return convert


def check_valid_choice(choice):
    """
    Check if player entered a valid choice.

    :param choice: a string
    :precondition: choice must be a string
    :postcondition: return True or False based on whether choice is valid or not
    :return: a boolean
    >>> check_valid_choice("rock")
    True
    >>> check_valid_choice("paper")
    True
    >>> check_valid_choice("scissors")
    True
    >>> check_valid_choice("asdasd")
    False
    >>> check_valid_choice("")
    False
    """
    if choice == "rock":
        result = True
    elif choice == "paper":
        result = True
    elif choice == "scissors":
        result = True
    else:
        result = False
    return result


def check_win(computer, player):
    """
    Check the result of the Rock, Paper, Scissors game.

    :param computer: a string
    :param player: a string
    :precondition: computer must be a string
    :precondition: player must be a string
    :postcondition: return the result of the game as a string
    :return: a string
    >>> check_win("rock", "rock")
    'tie'
    >>> check_win("rock", "paper")
    'win'
    >>> check_win("rock", "scissors")
    'lose'
    """
    if (computer == "rock" and player == "rock") or (computer == "paper" and player == "paper")\
            or (computer == "scissors" and player == "scissors"):
        result = "tie"
    elif (computer == "rock" and player == "paper") or (computer == "paper" and player == "scissors")\
            or (computer == "scissors" and player == "rock"):
        result = "win"
    elif (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock")\
            or (computer == "scissors" and player == "paper"):
        result = "lose"
    return result


def print_result(result):
    """
    Print result of Rock, Paper, Scissors game to screen.

    :param result: a string
    :precondition: result must be a string
    :postcondition: print a short message stating the result of the game
    >>> print_result("tie")
    Result: It's a tie!
    >>> print_result("win")
    Result: Congratulations, you won!
    >>> print_result("lose")
    Result: Sorry, you lost!
    """
    if result == "tie":
        print("Result: It's a tie!")
    elif result == "win":
        print("Result: Congratulations, you won!")
    elif result == "lose":
        print("Result: Sorry, you lost!")


def rock_paper_scissors():
    computer_choice = computer_choice_convert(random.randint(0, 2))
    player_choice = (input("Please pick \"Rock\", \"Paper\", or \"Scissors\": ")).strip().lower()

    if not check_valid_choice(player_choice):
        print("You've typed an invalid choice.")
    elif check_valid_choice(player_choice):
        print("The computer chose:", computer_choice.capitalize())
        print("You chose:", player_choice.capitalize())
        print_result(check_win(computer_choice, player_choice))


if __name__ == "__main__":
    doctest.testmod()
