def shellsort(inp):
    interval = 0

    while interval < len(inp):
        interval = interval * 3 + 1

    while interval > 0:
        for x in range(interval, len(inp)):
            insert = inp[x]
            left = x

            while left > interval - 1 and inp[left-interval] >= insert:
                inp[left] = inp[left-interval]
                left = left - interval

            inp[left] = insert

        interval = (interval - 1) // 3

    return inp


if __name__ == '__main__':

    from random import randrange

    start = 1
    end = 20

    nums = []
    while len(nums) <= end-start-1:
        x = randrange(start, end)
        if x not in nums:
            nums.append(x)

    print(f"Unsorted: {nums}")
    nums = shellsort(nums)
    print(f"Sorted  : {nums}")


""" Output
Unsorted: [17, 7, 14, 4, 13, 3, 12, 1, 9, 8, 10, 11, 18, 16, 19, 2, 6, 5, 15]
Sorted  : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""