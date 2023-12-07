import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    answer = str(gcd(num1, num2))
    return question, answer
