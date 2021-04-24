"""Even number guess game."""

from random import randint

from brain_games.games_engine import engine


def question():
    """Make Question number.

    Returns:
        int: Random number.
    """
    return randint(1, 1000)


def question_check(que):
    """Check if number is even.

    Args:
        que (int): Number

    Returns:
        str: 'yes' if number is even 'no' if else.
    """
    return 'yes' if que % 2 == 0 else 'no'


def build_and_play():
    """Build and play the game."""
    engine(DESCRIPTION, question, question_check)


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
