import random


DESCRIPTION = 'What number is missing in the progression?'


def arith_progression(n):
    a0 = random.randint(1, 100)
    d = random.randint(1, 100)
    a = []
    a.append(str(a0))
    for i in range(1, n):
        a.append(str(int(a[i - 1]) + d))
    return a


def generate_round():
    n = 10
    prog_list = arith_progression(n)
    hide_k = random.randint(0, n - 1)
    answer = prog_list[hide_k]
    prog_list[hide_k] = ".."
    question = ' '.join(prog_list)
    return question, answer
