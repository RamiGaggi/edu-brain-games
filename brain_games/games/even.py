"""Even-guess game."""

from random import randint as rand

from brain_games.games_engine import engine


def question():
    """Make Question number.

    Returns:
        int: Random number.
    """
    return rand(1, 1000)


def question_check(que):
    """Check if number even.

    Args:
        que (int): Number

    Returns:
        str: 'yes' if number even 'no' if else.
    """
    return 'yes' if que % 2 == 0 else 'no'


def build_and_play():
    """Build and play the game."""
    engine(description, question, question_check)


description = 'Answer "yes" if the number is even, otherwise answer "no".'