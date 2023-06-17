
from typing import List


def three_sum(nums: List[int]):
    nums.sort()
    n = len(nums)
    result = dict()
    for i in range(n-2):
        left = i+1
        right = n-1

        while left < right:
            a,b,c = nums[i], nums[left], nums[right]
            total = a+b+c

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result[(a,b,c)] = total
                left += 1
                right -= 1

    result = list(result)
    print(result)
    return result

lst = [-1,0,1,2,-1,-4]
three_sum(lst)
