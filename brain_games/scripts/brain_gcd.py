
import prompt
import random

ANSWERS_TO_WIN = 3


def calc_gcd(x: int, y: int) -> int:

    if x == y:
        return x
    if x > y:
        return calc_gcd(x - y, y)
    else:
        return calc_gcd(y, x)


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')

    right_answers = 0
    while True:
        x: int = random.randint(0, 1000)
        y: int = random.randint(0, 1000)

        print(f'Question: {x} {y}')
        answer = prompt.string("Your answer: ")

        corr = str(calc_gcd(x, y))
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
