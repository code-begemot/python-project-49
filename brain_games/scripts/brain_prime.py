from brain_games.scripts.game_logic import game, greet, welcome_user
import random


def is_prime(n):
    if n <= 1:
        return 'no'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'no'
        return 'yes'


def main():
    greet()
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    questions = []
    answers = []
    for i in range(3):
        questions.append(random.randint(1, 100))
        answers.append(is_prime(questions[i]))
    game(name, questions, answers)


if __name__ == "__main__":
    main()
