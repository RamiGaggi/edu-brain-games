"""Engine for all games."""
import prompt


def engine(desc, que, check):
    """Build the question-answer game with win condition eq 3.

    Args:
        desc (str): Description of the game.
        que (str/int): Question for the round of the game.
        check (func): Checkout answer for question.
    """
    name = prompt.string('May I have your name? ')
    print('Welcome to the Brain Games!')
    print('Hello, {0}!'.format(name))
    print(desc)  # var
    win_condition = 0
    while win_condition < 3:
        question = que()
        question_check = check(question)  # var
        print('Question:', question)
        answer = input('Your answer: ').lower().strip()
        if question_check == answer:
            print('Correct!')
            win_condition += 1
            continue
        print('"{answer}" is wrong answer ;(. Correct answer was "{que_check}".'.format(answer=answer, que_check=question_check))  # noqa: E501
        print("Let's try again, {name}!".format(name=name))
        return
    print('Congratulations, {name}!'.format(name=name))
