import prompt
from brain_games.games import cli


ATTEMPT = 3
# Question for games
QUESTION_CALC = 'What is the result of the expression?'
QUESTION_EVEN = 'Answer "yes" if the number is even otherwise answer "no".'
QUESTION_GCD = 'Find the greatest common divisor of given numbers.'
QUESTION_PRIME = ('Answer "yes" if given number is prime. '
                  'Otherwise answer "no".')
QUESTION_PROGRESSION = 'What number is missing in the progression?'


def engine(game, quest):
    name = cli.welcome_user()
    print(quest)
    for _ in range(ATTEMPT):
        question, correct_answer = game()
        print(f'Question: {question}')
        your_answer = prompt.string("Your answer: ")
        if str(your_answer) == correct_answer:
            print('Correct!')
        else:
            print(f"'{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
