import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n <= 1:
        return 'no'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'no'
        return 'yes'


def generate_round():
    num = random.randint(1, 100)
    question = num
    answer = is_prime(num)
    return question, answer
