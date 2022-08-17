from plus_one import plusOne


def test_single_digit_change():
    assert plusOne([1, 2, 3]) == [1, 2, 4]


def test_double_digit_change():
    assert plusOne([1, 2, 9]) == [1, 3, 0]


def test_len_equal_one():
    assert plusOne([9]) == [1, 0]
