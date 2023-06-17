- [Best Block](#BestBlock)
- [Two Sum](#TwoSum)
- [Generate Parantheses](#GenerateParantheses)



## BestBlock
## Problem Statement  

Given a list of blocks, each with specific attributes, the task is to find the best block that satisfies the given requirements.

## Input

The input consists of two main components:

-  `blocks`: A list of objects representing different blocks. Each dictionary contains attributes or features of a block.

-  `reqs`: A list of strings representing the required attributes that the best block must have.

 
## Output

 
The output is the index or key of the best block among the given list of blocks.

 
## Example:

In the given example, there are five blocks with their respective attributes. The required attributes are "gym", "school", and "store".

```python
blocks = [
{"gym": False, "school": True, "store": False},
{"gym": True, "school": False, "store": False},
{"gym": True, "school": True, "store": False},
{"gym": False, "school": True, "store": False},
{"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]
```

The correct answer is 3.
While Blocks 4 and 5 have the same summed distance, the number of block travels should be minimized. Block 3, however, has a lower number of block travels compared to Blocks 4 and 5. Here is a breakdown of the distances:

```
gym: = 1  # Distance to a valid Gym is 1 (at index 1)
school: 0  # Distance to a valid School is 0 (at index 0)
store: 4   # Distance to a valid Store is 4 (at index 4)

gym: 0
school: 1
store: 3

gym: 0
school: 0
store: 2

gym: 1
school: 0
store: 1

gym: 2
school: 0
store: 0
```






## TwoSum

### Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You need to return the indices of the two numbers in the original array, not the sorted order.

### Input

The input consists of two main components:

- `nums`: An array of integers representing the input numbers.
- `target`: An integer representing the target sum.

### Output

The output is an array of two integers, representing the indices of the two numbers that add up to the target sum.

### Example

Given the following input:

```python
nums =[11, 15, 16, 14, 2, 7]
target = 9
```

The correct answer is (4,5)




## GenerateParantheses

### Problem Statement
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Input

The input consists of:

- `n`: An integer such that 1 <= n <= 8

### Output

The output is an array of well-formed parentheses

### Example

```
Input: 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

