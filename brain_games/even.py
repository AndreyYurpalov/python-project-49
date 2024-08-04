import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 0
    sum_correct_answer = 0
    while attempt < 3:
        number = random.randint(1, 100)
        control = number % 2
        your_answer = prompt.string(f'Question {number}: ')
        if control == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if your_answer == correct_answer:
            print('Correct!')
            attempt += 1
            sum_correct_answer += 1
        else:
            attempt = 3
    if sum_correct_answer == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{your_answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
