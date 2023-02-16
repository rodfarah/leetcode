'''Given a roman numeral, convert it to an integer'''

letters_and_values_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def separate_values(lots_of_letters: str) -> list[int]:
    '''Creates a single list with absolute values of each letter'''
    separated_values = []
    for letter in lots_of_letters:
        for k, v in letters_and_values_dict.items():
            if k == letter:
                separated_values.append(v)
    return separated_values


def slice_iterator(data, slice_len):
    '''Slices the above list of values, 3 by 3. Less if remainder'''
    it = iter(data)
    while True:
        items = []
        for index in range(slice_len):
            try:
                item = next(it)
            except StopIteration:
                if items == []:
                    return
                else:
                    break
            items.append(item)
        yield items


def only_one(list_of_one: list[int]) -> int:
    ''' if the slice contains only 1 number'''
    return sum(list_of_one)


def only_two(list_of_two: list[int]) -> int:
    ''' if the slice contains only 2 numbers'''
    if list_of_two[0] >= list_of_two[1]:
        return sum(list_of_two)
    return list_of_two[1] - list_of_two[0]


def only_three(list_of_three: list[int]) -> int:
    ''' if the slice contains 3 numbers (max)'''

    accumulator = []
    if list_of_three[0] >= list_of_three[1] >= list_of_three[2]:
        return sum(list_of_three)
    elif list_of_three[0] < list_of_three[1] > list_of_three[2]:
        return list_of_three[1] - list_of_three[0] + list_of_three[2]
    elif list_of_three[0] > list_of_three[1] < list_of_three[2]:
        return list_of_three[0] + (list_of_three[2] - list_of_three[1])
    


def roman_to_int(s: str) -> int:
    '''The fundamental function'''
    first_step = separate_values(s)

    print(list(slice_iterator(first_step, 3)))
    accumulated_list = []
    for slice in slice_iterator(first_step, 3):
        if len(slice) == 1:
            accumulated_list.append(only_one(slice))
        elif len(slice) == 2:
            accumulated_list.append(only_two(slice))
        elif len(slice) == 3:
            accumulated_list.append(only_three(slice))
    return sum(accumulated_list)


# print(roman_to_int('M'))
# print(roman_to_int('MM'))
# print(roman_to_int('CD'))
# print(roman_to_int('DC'))
# print(roman_to_int('III'))
# print(roman_to_int('XCI'), 91)
# print(roman_to_int('LVIII'))
print(roman_to_int('MCMXCIV'))
# print(roman_to_int('MMXXIII'), 2023)
# print(roman_to_int('MCMXCVI'), 1996)
# print(roman_to_int('MCMXCVIII'), 1998)
# print(roman_to_int('MMXXVIII'), 2028)
