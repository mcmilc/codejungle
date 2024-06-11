def find_two_max(arr):
    largest = arr[0]
    second_largest = arr[0]
    for item in arr:
        if item > largest:
            second_largest = largest
            largest = item
        elif item > second_largest and item != largest:
            second_largest = item
    return largest, second_largest


if __name__ == "__main__":
    n_items = input()
    in_vals = input().split()
    array = list(map(int, in_vals))
    x1, x2 = find_two_max(array)
    print(x1 * x2)
