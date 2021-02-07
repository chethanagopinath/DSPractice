def magic_index(arr):
    return binary_search(0, len(arr) - 1, arr)


def binary_search(start, end, arr):
    # base case
    # positive - arr[mid] == mid
    # negative - start reaches the end of the input

    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid

    elif arr[mid] > mid:
        return binary_search(start, mid - 1, arr)

    elif arr[mid] < mid:
        return binary_search(mid + 1, end, arr)


if __name__ == '__main__':
    print(magic_index([-14, -12, 0, 1, 2, 5, 5, 10, 23, 25]))
    # [-14, -12, 0, 1, 5, 5, 9, 10, 23, 25] => binary search will break for this test case
    # do the follow up properly
