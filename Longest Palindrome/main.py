from plotter import plot
from approach_1 import longest_palindrome as longest_palindrome1
from approach_2 import longest_palindrome as longest_palindrome2
from approach_3 import longest_palindrome as longest_palindrome3
import random


def random_input(n):
    s = ""
    for _ in range(n):
        s += chr(random.randint(97, 122))
    return s,


plot(
    "Longest Palindrome",
    random_input,
    longest_palindrome1,
    longest_palindrome2,
    longest_palindrome3,
)
