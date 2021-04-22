"""Even-guess game."""

from random import randint as rand


def even_game(name):
    """Start the game, guess even number with win condition.

    Args:
        name (str): The name of the player.
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    win_condition = 3
    while count != win_condition:
        question = rand(1, 1000)
        even_check = 'yes' if question % 2 == 0 else 'no'
        print('Question: ', question)
        answer = input('Your answer: ').lower().strip()
        if even_check == answer:
            print('Correct!')
            count += 1
            continue
        print('"yes" is wrong answer ;(. Correct answer was "no".')
        return
    print('Congratulations, {name}!'.format(name=name))
