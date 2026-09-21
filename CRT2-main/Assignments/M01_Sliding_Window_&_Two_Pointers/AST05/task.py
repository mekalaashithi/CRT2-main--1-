def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    # Product of elements to the left
    left_product = 1
    for i in range(n):
        res[i] = left_product
        left_product *= nums[i]

    # Product of elements to the right
    right_product = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]

    return res


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(productExceptSelf(arr))