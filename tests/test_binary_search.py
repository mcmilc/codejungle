from ..algorithms.binary_search import binary_search


def test_ordered_list():
    a = [x for x in range(50, 150)]
    n = 67
    result = binary_search(sorted_array=a, n=n)
    print(result)
    assert result == 17


if __name__ == "__main__":
    test_ordered_list()
