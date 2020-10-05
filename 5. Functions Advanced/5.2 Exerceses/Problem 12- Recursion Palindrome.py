

def palindrome(word, index=0):
    if index >= len(word) // 2:
        return f"{word} is a palindrome"

    if word[0] == word[-1]:
        return palindrome(word, index + 1)

    return f"{word} is not a palindrome"


# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
