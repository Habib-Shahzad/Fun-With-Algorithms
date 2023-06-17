
def longest_substring(s: str, debug=False):

    best_length = 0
    start = 0
    visited = dict()

    for index, char in enumerate(s):
        if visited.get(char) is not None:
            start = max(visited[char]+1, start)

        visited[char] = index
        end = index+1
        best_length = max(best_length, end-start)

        if debug:
            substring = s[start:end]
            print(substring)

    return best_length


# s = "abcabcbb"
# s = "pwwpkew"
# s = "pu"
# s = "jyercvgdyix"
# print(longest_substring(s, True))
