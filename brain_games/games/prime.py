"""Prime number guess game."""

from random import randint

from brain_games.games_engine import engine


def question():
    """Generate random int number.

    Returns:
        int: Random number.
    """
    return randint(0, 100)


def question_check(que):
    """Check if number is prime starting from 2.

    Args:
        que (int): Number

    Returns:
        str: 'yes' if number is prime 'no' if else.
    """
    for num in range(2, que):
        if que % num == 0:
            return 'no'
    return 'yes'


def build_and_play():
    """Build and play the game."""
    engine(description, question, question_check)


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
