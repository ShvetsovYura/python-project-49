import prompt
import random

ANSWERS_TO_WIN = 3


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    right_answers = 0
    while True:
        val: int = random.randint(0, 1000)
        print(f'Question: {val}')
        answer = prompt.string("Your answer: ")

        # if answer not in (s'yes', 'no'):
        corr = 'yes' if val % 2 == 0 else 'no'
        if (corr == answer):
            print('Correct!')
            right_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{corr}'.")
            print(f"Let's try again, {name}!")
            return

        if right_answers > 2:
            print(f'Congratulations, {name}!')
            return


if __name__ == '__main__':
    main()
