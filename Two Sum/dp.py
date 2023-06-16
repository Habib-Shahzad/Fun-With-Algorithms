from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    table = dict()

    for index, num in enumerate(nums):
        possible_index = table.get(num, None)
        if possible_index is not None:
            return (possible_index, index)

        difference = target - num
        table[difference] = index
