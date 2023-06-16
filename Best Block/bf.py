from typing import List, Dict
from math import inf


def get_best_block(blocks: List[Dict], reqs: List[str], debug=False):

    class BlockReqs:
        def __init__(self) -> None:
            self.scores: Dict = dict()

        def update(self, block_number):
            for req in reqs:
                block = blocks[block_number]
                if block[req] == True:
                    prev_score = self.scores.get(req, inf)
                    score = abs(current_block_number - block_number)
                    self.scores[req] = min(prev_score, score)

        def get_max(self):
            return max(list(self.scores.values()))

        def get_sum(self):
            return sum(list(self.scores.values()))

        def __gt__(self, other: 'BlockReqs'):
            m1 = self.get_max()
            m2 = other.get_max()

            s1 = self.get_sum()
            s2 = other.get_sum()

            if s1 == s2:
                return m1 > m2

            return s1 > s2

        def __repr__(self) -> str:
            result = ""
            for req in reqs:
                result += f"{req}: {self.scores.get(req)}\n"

            return result

    num_blocks = len(blocks)
    all_block_reqs: Dict[int, BlockReqs] = dict()

    for current_block_number in range(num_blocks):
        current_block_reqs = BlockReqs()

        # Backward Traversal
        for block_number in range(current_block_number, -1, -1):
            current_block_reqs.update(block_number)

        # Forward Traversal
        for block_number in range(current_block_number, num_blocks):
            current_block_reqs.update(block_number)

        all_block_reqs[current_block_number] = current_block_reqs

    key = min(all_block_reqs.keys(), key=lambda x: all_block_reqs[x])
    if debug:
        print(all_block_reqs[key])
    return key
