def longestCommonPrefix(strs: list[str]) -> str:
    combined_letters = list(zip(*strs))

    result = ''
    for combination in combined_letters:
        if len(set(combination)) == 1:
            result += combination[0]
        else:
            break
    return result

