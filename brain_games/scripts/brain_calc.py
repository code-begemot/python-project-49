from brain_games.scripts.game_logic import game, greet, welcome_user
import random

def main():  
    greet()
    name = welcome_user()
    print('What is the result of the expression?')        
    questions = []
    answers = []
    for i in range(3):
        questions.append(f'{random.randint(1, 100)} {random.choice(["+", "-", "*"])} {random.randint(1, 100)}')
        answers.append(str(eval(questions[i])))
    game(name, questions, answers)
		               
if __name__ == "__main__":
    main()
