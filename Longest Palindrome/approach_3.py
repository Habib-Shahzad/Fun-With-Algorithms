

# Manacher's Algorithm
def longest_palindrome(s: str):
    modified_s = '#'.join(f'^{s}$')

    n = len(modified_s)
    p = [0] * n
    center = right = max_len = max_center = 0
    
    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        
        while modified_s[i + 1 + p[i]] == modified_s[i - 1 - p[i]]:
            p[i] += 1
        
        if i + p[i] > right:
            center = i
            right = i + p[i]
        
        if p[i] > max_len:
            max_len = p[i]
            max_center = i
    
    start = (max_center - max_len) // 2
    end = start + max_len

    return s[start:end]


s = "babad"
print(longest_palindrome(s))