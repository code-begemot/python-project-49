import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def odd_even_check(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_round():
    num = random.randint(1, 100)
    question = num
    answer = odd_even_check(num)
    return question, answer
