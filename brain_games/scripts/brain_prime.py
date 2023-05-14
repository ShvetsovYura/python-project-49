import prompt
import random

ANSWERS_TO_WIN = 3


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(1, n):
        if n % i == 0:
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    right_answers = 0
    while True:
        val: int = random.randint(0, 100)
        print(f'Question: {val}')
        answer = prompt.string("Your answer: ")

        corr = 'yes' if is_prime(val) else 'no'
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
