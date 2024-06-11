def find_two_max(arr):
    assert len(arr) > 1
    if arr[0] > arr[1]:
        largest = arr[0]
        second_largest = arr[1]
    else:
        largest = arr[1]
        second_largest = arr[0]
    for item in arr[2:]:
        if item > largest:
            second_largest = largest
            largest = item
        elif item > second_largest:
            second_largest = item
    return largest, second_largest


if __name__ == "__main__":
    n_items = input()
    in_vals = input().split()
    array = list(map(int, in_vals))
    x1, x2 = find_two_max(array)
    print(x1 * x2)
