from array2D import slice_me


def test_valid_cases():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(f"Initial List: {family}")
    print("Test 1 : slice_me(family, 0, 2)")
    print(slice_me(family, 0, 2))  # [[1.8, 78.4], [2.15, 102.7]]

    print("Test 2 : slice_me(family, 1, -2)")
    print(slice_me(family, 1, -2))  # [[2.15, 102.7]]


def test_invalid_cases():
    print("\nTest 3 : family is not a list")
    try:
        slice_me("not a list", 0, 2)
    except Exception as e:
        print("Caught exception:", e)

    print("\nTest 4 : family contains non-list elements")
    try:
        slice_me([1.80, 2.15, 2.10], 0, 2)
    except Exception as e:
        print("Caught exception:", e)

    print("\nTest 5 : family rows have inconsistent sizes")
    try:
        slice_me([[1.80, 78.4], [2.15], [2.10, 98.5]], 0, 2)
    except Exception as e:
        print("Caught exception:", e)


if __name__ == "__main__":
    test_valid_cases()
    test_invalid_cases()
