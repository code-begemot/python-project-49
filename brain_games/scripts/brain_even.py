from brain_games.scripts.game_logic import game, greet, welcome_user
import random

def odd_even_check(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    greet()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    questions = []
    answers = []
    for i in range(3):
    	questions.append(random.randint(1, 1000))
    	answers.append(odd_even_check(questions[i]))
    game(name, questions, answers)

if __name__ == "__main__":
    main()
