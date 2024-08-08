import prompt


def welcome_user(dic_res, game_cycle):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(dic_res.get('question'))
    attempt = 0
    sum_correct_answer = 0
    while attempt < 3:
        game_cycle()
        print(f"Question: {dic_res.get('number')}")
        your_answer = prompt.string("Your answer: ")
        if str(your_answer) == str(dic_res.get('correct_answer')):
            print('Correct!')
            attempt += 1
            sum_correct_answer += 1
        else:
            attempt = 3
    if sum_correct_answer == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{your_answer}' is wrong answer ;(."
              f"Correct answer was '{dic_res.get('correct_answer')}'")
        print(f"Let's try again, {name}!")
