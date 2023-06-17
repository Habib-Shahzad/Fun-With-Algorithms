
from plotter import plot
from bf import longest_substring as bf_longest_substring
from dp import longest_substring as dp_longest_substring
import random


def generate_random_string(n):
    s = ""
    for _ in range(n):
        s += chr(random.randint(97, 122))
    return s,


def test():
    for i in range(1000):
        x = generate_random_string(i)

        a = bf_longest_substring(x)
        b = dp_longest_substring(x)

        if a != b:
            print("OOPS")
            print(a, b, x)
            return


plot("Longest Substring",
     generate_random_string,
     bf_longest_substring,
     dp_longest_substring)
