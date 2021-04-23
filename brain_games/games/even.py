"""Even-guess game."""

from random import randint as rand

from brain_games.games_engine import engine


def question():
    """[summary].

    Returns:
        [type]: [description]
    """
    return rand(1, 1000)


def question_check(que):
    """[summary].

    Args:
        que ([type]): [description]

    Returns:
        [type]: [description]
    """
    return 'yes' if que % 2 == 0 else 'no'


def build_and_play():
    """[summary]."""
    engine(description, question, question_check)


description = 'Answer "yes" if the number is even, otherwise answer "no".'
