import random


DESCRIPTION = "What is the result of the expression?"


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    question = f'{num1} {operator} {num2}'
    answer = str(eval(question))
    return question, answer
