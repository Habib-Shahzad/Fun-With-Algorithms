
from bf import two_sum as bf_func
from dp import two_sum as dp_func
import random
from plotter import plot


def generate_random_input(n):
    nums = list(range(n))
    random.shuffle(nums)
    target = random.randint(0, 2 * n)
    return nums, target


plot("Two Sum",
     generate_random_input,
     bf_func,
     dp_func)
