'''Given a roman numeral, convert it to an integer'''


def romanToInt(s: str) -> int:

    letters_and_values_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')

    each_letter_value = []
    for letter in s:
        each_letter_value.append(letters_and_values_dict.get(letter))

    return sum(each_letter_value)
