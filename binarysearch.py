def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    if binary_search(nums, 7, 0, len(nums) - 1) == True:
        print("Found it!")
    else:
        print("Not found")


def binary_search(nums, target, low, high):
    if low > high:
        return False
    else:
        mid = round((low + high) / 2)
        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            return binary_search(nums, target, low, mid - 1)
        else:
            return binary_search(nums, target, mid + 1, high)

main()