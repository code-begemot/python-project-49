import random
import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game(name, questions, answers):
    for i in range(3):
        print(f'Question: {questions[i]}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answers[i]:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answers[i]}.\nLet's try again, {name}!")
            return 0
    print(f'Congratulations, {name}!')
    return 1
    

