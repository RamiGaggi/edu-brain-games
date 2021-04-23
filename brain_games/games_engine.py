"""Engine for all games."""
import prompt


def engine(desc, que, check):
    """[summary].

    Args:
        desc (str): [description]
        que (str): [description]
        check (func): [description]
    """
    name = prompt.string('May I have your name? ')
    print('Welcome to the Brain Games!')
    print('Hello, {0}!'.format(name))
    print(desc)  # var
    win_condition = 0
    while win_condition < 3:
        question = que()
        question_check = check(question)  # var
        print('Question: ', question)
        answer = input('Your answer: ').lower().strip()
        if question_check == answer:
            print('Correct!')
            win_condition += 1
            continue
        print('"{answer}" is wrong answer ;(.Correct answer was "{que_check}".'.format(answer=answer, que_check=question_check))  # noqa: E501
        return
    print('Congratulations, {name}!'.format(name=name))
