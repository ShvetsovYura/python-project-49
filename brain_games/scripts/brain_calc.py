
import prompt
import random

ANSWERS_TO_WIN = 3


def add(x: int, y: int) -> int:
    return x + y


def prod(x: int, y: int) -> int:
    return x * y


def sub(x: int, y: int) -> int:
    return x - y


opers = {
    '+': add,
    '*': prod,
    '-': sub,
}


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')

    right_answers = 0
    while True:
        x: int = random.randint(0, 1000)
        y: int = random.randint(0, 1000)
        oper = random.choice(list(opers.keys()))

        print(f'Question: {x} {oper} {y}')
        answer = prompt.string("Your answer: ")

        corr = opers[oper](x, y)
        if (str(corr) == answer):
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
