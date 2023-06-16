

from bf import two_sum as bf_two_sum
from dp import two_sum as dp_two_sum

nums = [11, 15, 16, 14, 2, 7]
target = 9


nums = [17, 11, 16, 10, 19, 18, 6, 13]
target = 30


print(bf_two_sum(nums, target))
print(dp_two_sum(nums, target))
