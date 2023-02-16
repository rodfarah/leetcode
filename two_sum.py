def twoSum(nums: list[int], target: int) -> list[int]:
    same_nums_list = nums.copy()
    same_nums_dict = {k: v for k, v in enumerate(same_nums_list, 0)}

    if len(nums) == 2 and sum(nums) == target:
        return [0, 1]
    else:
        for num in nums:
            same_nums_list.remove(num)
            for n in same_nums_list:
                if num + n == target:
                    chosen_nums = [num, n]
    index_list = []
    for k, v in same_nums_dict.items():
        if v in chosen_nums:
            index_list.append(k)

    return index_list


print(twoSum([3, 2, 3], 6))
