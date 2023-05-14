
import prompt
import random

ANSWERS_TO_WIN = 3


def make_progression(start: int, end: int, step: int) -> list[str]:
    return [str(el) for el in range(start, end, step)][:10]


def main():
    print('Welcome to the Brain Games!')
    name = 'hoho'  # prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What number is missing in the progression?')

    right_answers = 0
    while True:

        while True:
            x: int = random.randint(0, 1000)
            y: int = random.randint(0, 1000)
            z: int = random.randint(1, 13)
            prog = make_progression(x, y, z)
            if len(prog) > 5:
                break
        rand_idx = random.randint(0, len(prog)-1)
        corr = prog[rand_idx]
        prog[rand_idx] = '..'
        prog_ = ' '.join(prog)

        print(f'Question: {prog_}')
        answer = prompt.string("Your answer: ")

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
