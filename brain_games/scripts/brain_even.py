import random
import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def odd_even_check(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def odd_even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        rand_num = random.randint(1, 1000)
        right_answer = odd_even_check(rand_num)
        user_answer = prompt.string(f'Question: {rand_num}\nYour answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            return f"{user_answer} is wrong answer ;(. Correct answer was\
             {right_answer}./nLet's try again, Bill!"
    return f'Congratulations, {name}!'


def main():
    greet()
    name = welcome_user()
    result = odd_even_game(name)
    print(result)


if __name__ == "__main__":
    main()
