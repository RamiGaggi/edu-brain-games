"""All prints."""
import prompt


def welcome_user():
    """
    Greet user with input name.

    Returns:
        str: name
    """
    name = prompt.string('May I have your name? ')
    print('Welcome to the Brain Games!')
    print('Hello, {0}!'.format(name))
    return name
