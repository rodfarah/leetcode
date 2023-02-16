'''Given an integer x, return true if x is a palindrome and false otherwise.'''


def isPalindrome(x: int) -> bool:
    x = str(x)
    return x == x[::-1]


print(isPalindrome(1212))
