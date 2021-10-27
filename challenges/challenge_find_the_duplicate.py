from typing import Counter


def find_duplicate(nums):
    """Retorna o número mais duplicado."""
    if nums == "" or len(nums) < 2:
        return False

    if str in nums:
        return False

    if _is_positive_number(nums) is not True:
        return False

    return _count_duplicate(nums)


def _count_duplicate(nums):
    rep_count = []

    for num, count in Counter(nums).items():
        if count > 1:
            rep_count.append(num)
            if len(rep_count) > 1:
                return False

    if len(rep_count) == 0:
        return False

    return rep_count[0]


def _is_positive_number(nums):
    for num in nums:
        try:
            if num < 1:
                return False
        except TypeError:
            return False

    return True


# nums = [1, 2]
# print(find_duplicate(nums))
