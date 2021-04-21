"""Cli functions."""

import prompt


def welcome_user():
    """
    Greet user with input name.

    Returns:
        str: name
    """
    return prompt.string('May I have your name? ')
