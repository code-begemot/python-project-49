from brain_games.scripts.game_logic import game, greet, welcome_user
import random

def arith_progression(n):
    a0 = random.randint(1, 100)
    d = random.randint(1, 100)
    a = []
    a.append(str(a0))
    for i in range(1, n):
        a.append(str(int(a[i - 1]) + d))
    return a

def main():  
    n = 10
    greet()
    name = welcome_user()
    print('What number is missing in the progression?')        
    questions = []
    answers = []
    temp_list = []
    for i in range(3):
        temp_list = arith_progression(n)
        hide_k = random.randint(1, n)
        answers.append(temp_list[hide_k])
        temp_list[hide_k] = ".."
        questions.append(' '.join(temp_list))
    game(name, questions, answers)
		               
if __name__ == "__main__":
    main()
