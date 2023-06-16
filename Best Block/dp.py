from typing import List, Dict
from enum import Enum
from math import inf


def get_best_block(blocks: List[Dict], reqs: List[str], debug=False):
    num_blocks = len(blocks)

    class BlockReqs:
        def __init__(self) -> None:
            self.scores: Dict = dict()

        def update(self, req, score):
            previous_score = self.scores.get(req, inf)
            self.scores[req] = min(score, previous_score)

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

    all_block_reqs: Dict[int, BlockReqs] = dict()

    class TraverseDirection(Enum):
        FORWARD = range(num_blocks)
        BACKWARD = range(num_blocks-1, -1, -1)

    def update_distances(direction: TraverseDirection):
        for req in reqs:
            last_seen = None
            for i in direction.value:
                block = blocks[i]
                if all_block_reqs.get(i) is None:
                    all_block_reqs[i] = BlockReqs()
                if block[req]:
                    last_seen = i
                if last_seen is not None:
                    score = abs(i - last_seen)
                    all_block_reqs[i].update(req, score)

    update_distances(TraverseDirection.FORWARD)   # Forward Traversal
    update_distances(TraverseDirection.BACKWARD)  # Backward Traversal

    key = min(all_block_reqs.keys(), key=lambda x: all_block_reqs[x])
    if debug:
        print(all_block_reqs[key])
    return key
