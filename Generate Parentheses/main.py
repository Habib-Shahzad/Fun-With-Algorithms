from plotter import plot
from approach_1 import generate_parentheses as gen_parantheses1
from approach_2 import generate_parentheses as gen_parantheses2


def random_input(n):
    return n,


def is_valid(s: str):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        if bracket == ')':
            stack.pop()

    return len(stack) == 0


# for i in range(1, 10):
#     x = gen_parantheses1(i)
#     y = gen_parantheses2(i)

plot(
    "Generate Parantheses",
    random_input,
    gen_parantheses1,
    gen_parantheses2
)