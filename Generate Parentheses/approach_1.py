

def generate_parentheses(n: int):
    result = []
    queue = [('(', 1, 0)]

    while queue:
        # s: current combination of brackets
        # left: count of open brackets
        # right: count of closed brackets
        s, left, right = queue.pop(0)
        
        if len(s) == 2*n:
            result.append(s)

        if left < n:
            queue.append((s + '(', left + 1, right))
        if right < left:
            queue.append((s + ')', left, right + 1))

    return result
