def bsearch(val, arr):
    """
    Binary search
    Assuming the array is sorted, else
    use arr.sort() before searching.
    Assuming there are no duplicates.
    """

    if not arr:
        return

    l,r = 0, len(arr)-1

    while l <= r:
        m = l + ((r-l) // 2)
        if val == arr[m]:
            return m
        if val < arr[m]:
            r = m-1
        else:
            l = m+1

    return -1

if __name__=="__main__":

    array = [x for x in range(10)]

    for x in array:
        print(f"found {x} at index {bsearch(x, array)}")

    print(f"found {5.5} at index {bsearch(5.5, array)}")