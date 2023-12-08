import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def odd_even_check(number):
    if number % 2 == 0:
        return True
    else:
        return False


def generate_round():
    num = random.randint(1, 100)
    question = num
    if odd_even_check(num):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
