
from bf import get_best_block as bf_get_best_block
from dp import get_best_block as dp_get_best_block
import random
from plotter import plot


def generate_random_input(n):
    possible_reqs = ["gym", "school", "store",
                     "office", "hospital", "nursery", "lake"]
    blocks = []
    for _ in range(n):
        block = {}
        for req in possible_reqs:
            block[req] = random.choice([True, False, False, False])
        blocks.append(block)

    reqs = random.sample(possible_reqs, random.randint(1, len(possible_reqs)))
    return blocks, reqs


def test():
    iterations = list(range(10, 1000, 100))
    for n in iterations:
        random_input = generate_random_input(n)
        x = bf_get_best_block(*random_input)
        y = dp_get_best_block(*random_input)

        if x != y:
            print("Failed")
            print(random_input)
            print(x, y)
            exit()


test()

# plot("Best Block",
#      generate_random_input,
#      bf_get_best_block,
#      dp_get_best_block)
