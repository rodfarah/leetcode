'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''


def isValid(s: str) -> bool:
    # based on veeannzhang's solution:
    open_close = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

    test = []
    for signal in s:
        if signal in open_close.keys():
            test.append(signal)
        elif len(test) == 0 or open_close[test.pop()] != signal:
            return False
    return len(test) == 0


print(isValid("[](){}"))
