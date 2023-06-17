

def longest_palindrome(s: str):
    longest = ''
    num_chars = len(s)
    table = dict()

    for i in range(num_chars):
        table[i, i] = True

    for i in range(num_chars-1, -1, -1):
        for j in range(i+1, num_chars):
            if s[i] == s[j]:
                if j-i == 1 or table.get((i+1, j-1), False) is True:
                    table[i, j] = True
                    if len(longest) < len(s[i:j+1]):
                        longest = s[i:j+1]

    return longest

