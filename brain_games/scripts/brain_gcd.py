from brain_games.scripts.game_logic import game, greet, welcome_user
import random


def gcd(my_list):
    a = int(my_list[0])
    b = int(my_list[1])
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def main():
    greet()
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    questions = []
    answers = []
    for i in range(3):
        questions.append(f'{random.randint(1, 100)} {random.randint(1, 100)}')
        answers.append(str(gcd(questions[i].split())))
    game(name, questions, answers)


if __name__ == "__main__":
    main()
