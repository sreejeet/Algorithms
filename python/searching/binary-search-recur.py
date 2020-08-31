def bsearch(val, arr, l, r):
    """
    Binary search
    Assuming the array is sorted, else
    use arr.sort() before searching.
    Assuming there are no duplicates.
    """

    if l > r:
        return -1

    m = l + ((r-l)//2)
    if val == arr[m]:
        return m
    elif val > arr[m]:
        return bsearch(val, arr, m+1, r)
    else:
        return bsearch(val, arr, l, m-1)


if __name__=="__main__":

    array = [x for x in range(10)]

    for x in array:
        print(f"found {x} at index {bsearch(x, array, 0, len(array))}")

    print(f"found {5.5} at index {bsearch(5.5, array, 0, len(array))}")