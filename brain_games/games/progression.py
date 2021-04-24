"""Arithmetic progression game."""

from random import randint

from brain_games.games_engine import engine


def question():
    """Generate arithmetic progression with  1 missing number.

    Returns:
        str: Arithmetic progression with  1 missing number.
    """
    progress_len = 10
    start = randint(1, 100)
    step = randint(1, 5)
    stop = start + step * progress_len
    progress = [str(num) for num in range(start, stop, step)]
    progress[randint(0, 9)] = '..'
    return ' '.join(progress)


def question_check(que):  # noqa: WPS210 it's possible to have 6 local variables
    """Checkout missing number.

    Args:
        que (str): Arithmetic progression with  1 missing number.

    Returns:
        str: missing number in arithmetic progression
    """
    progress = que.split()
    miss = progress.index('..')
    right_num = int(progress[(miss + 1) % len(progress)])
    right2_num = int(progress[(miss + 2) % len(progress)])
    left_num = int(progress[miss - 1])
    left_num2 = int(progress[miss - 2])

    if miss == 0:
        return str(right_num * 2 - right2_num)
    if miss == len(progress) - 1:
        return str(left_num * 2 - left_num2)
    return str(int((left_num + right_num) / 2))


def build_and_play():
    """Build and play the game."""
    engine(description, question, question_check)


description = 'What number is missing in the progression?'
