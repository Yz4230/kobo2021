# Tested in Python 3.9
# If not working, remove delete all type hints.

from typing import Callable
import numpy as np


def AND(x1: int, x2: int):
    x = np.array([x1, x2])
    w = np.array([[0.5], [0.5]])
    b = np.array([0])
    y = x.dot(w) + b
    return y.astype(np.int32)[0]


def NAND(x1: int, x2: int):
    return int(not AND(x1, x2))


def OR(x1: int, x2: int):
    x = np.array([x1, x2])
    w = np.array([[1], [1]])
    b = np.array([0])
    y = x.dot(w) + b
    return int(y.astype(np.int32)[0] > 0)


def XOR(x1: int, x2: int):
    return AND(NAND(x1, x2), OR(x1, x2))


if __name__ == '__main__':
    functions: Callable[[int, int], int] = [AND, NAND, OR, XOR]
    inputs = [[0, 0], [1, 0], [0, 1], [1, 1]]
    answers = {
        AND: [0, 0, 0, 1],
        NAND: [1, 1, 1, 0],
        OR: [0, 1, 1, 1],
        XOR: [0, 1, 1, 0]
    }
    for func in functions:
        for index, answer in enumerate(answers[func]):
            args: list = inputs[index]
            result = func(*args)

            # Start testing
            args_str = ', '.join(list(map(str, args)))
            result_str = f'{func.__name__}({args_str}) -> {result}'
            if result == answer:
                print(f'Passed {result_str}')
            else:
                print(
                    f'Failed {result_str}; expected {answer}')
