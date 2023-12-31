import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_logic(module):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    count = 0
    print(module.DESCRIPTION)
    while count < 3:
        question, answer = module.generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"{user_answer} is wrong answer ;(.Correct answer was\
 {answer}.\nLet's try again, {name}!")
            return 0
    print(f'Congratulations, {name}!')
    return 1
