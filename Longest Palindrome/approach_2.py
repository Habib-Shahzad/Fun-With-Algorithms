
def longest_palindrome(s: str):

    len_string = len(s)
    
    start = 0
    maxLength = 1
    
    for index in range(len_string):
        low = index - 1
        high = index + 1
        
        while (high < len_string and s[high] == s[index]):
            high = high + 1

        while (low >= 0 and s[low] == s[index]):
            low = low - 1

        while (low >= 0 and high < len_string and s[low] == s[high]):
            low = low - 1
            high = high + 1

        length = high - low - 1

        if (maxLength < length):
            maxLength = length
            start = low + 1

    return s[start:start + maxLength]



s = "babad"
s = "cbbd"
print(longest_palindrome(s))