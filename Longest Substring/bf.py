

# Runs in O(n^2)
def longest_substring(s: str, debug=False):
    
    num_chars = len(s)
    best_length = 0
    for index in range(num_chars):
        possible_sub = s[index:]
        substring = ""
        count = 0
        for char in possible_sub:
            if char not in substring:
                substring += char
                count += 1
            else:
                break
        
        if debug: print(substring)
        best_length = max(count, best_length)
        
    return best_length




# s = "abcabcbb"
# s = "pu"
# s = "pwpkew"
# s = "pwwpkew"
# s = "jyercvgdyix"
# print(longest_substring(s, True))

