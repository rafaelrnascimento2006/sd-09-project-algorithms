

def find_duplicate(nums):

    if len(nums) < 2 or type(nums[0]) is str:
        return False

    nums.sort()
    x = False
    for index in range(len(nums)-1):
        if nums[index + 1] == nums[index]:
            return nums[index]
        x = False

    return x


num = [1, 2]

print(find_duplicate(num))
