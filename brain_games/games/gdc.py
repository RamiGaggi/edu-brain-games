"""Game - find the greatest common divisor ."""
from random import randint

from brain_games.games_engine import engine


def question():
    """Generate two random numbers.

    Returns:
        str: Two random numbers with sep=' '.
    """
    return '{0} {1}'.format(randint(1, 100), randint(1, 100))


def question_check(que):
    """Find the greatest common divisor for 2 numbers.

    Args:
        que (str): Two numbers with sep=' '.

    Returns:
        str: divisor.
    """
    que = list(map(int, que.split()))
    min_num = min(que)
    max_num = max(que)
    divisor = 1
    for div in range(2, min_num + 1):
        if min_num % div == 0 and max_num % div == 0:
            divisor = div
    return str(divisor)


def build_and_play():
    """Build and play the game."""
    engine(description, question, question_check)


description = 'Find the greatest common divisor of given numbers.'
