def upper_bound(arr, x):
    """
    Returns index of first element > x
    If not found, returns len(arr)
    """
    low, high = 0, len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    arr = [1, 4, 6, 10, 13]
    x = 6
    print("Upper Bound Index:", upper_bound(arr, x))
