"""Calculator game."""

from random import choice, randint

from brain_games.games_engine import engine


def question():
    """Generate random mathematical expression.

    Returns:
        str: Mathematical expression.
    """
    rand_num = lambda: str(randint(1, 100))  # noqa: E731
    return '{0} {1} {2}'.format(rand_num(), choice('+*-'), rand_num())


def question_check(que):
    """Check mathematical expression.

    Args:
        que (str): Mathematical expression.

    Returns:
        int: Sum, sub, product of numbers.
    """
    num1, math_operator, num2 = [int(el) if el not in '+*-' else el for el in que.split()]  # noqa: WPS221, E501

    if math_operator == '*':
        return str(num1 * num2)
    if math_operator == '+':
        return str(num1 + num2)
    if math_operator == '-':
        return str(num1 - num2)


def build_and_play():
    """Build and play the game."""
    engine(description, question, question_check)


description = 'What is the result of the expression?'
