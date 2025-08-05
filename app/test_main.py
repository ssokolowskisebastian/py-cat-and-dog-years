from app.main import get_human_age


def test_get_human_age_should_be_equal_to_zero_lower_boundary() -> None:
    cat_age = 0
    dog_age = 0
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_get_human_age_should_be_equal_to_zero_upper_boundary() -> None:
    cat_age = 14
    dog_age = 14
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_get_human_age_should_be_equal_to_one_lower_boundary() -> None:
    cat_age = 15
    dog_age = 15
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_get_human_age_should_be_equal_to_one_upper_boundary() -> None:
    cat_age = 23
    dog_age = 23
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_get_human_age_should_be_equal_to_two_lower_boundary() -> None:
    cat_age = 24
    dog_age = 24
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_get_human_age_should_be_equal_to_two_upper_boundary() -> None:
    cat_age = 27
    dog_age = 28
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_get_human_age_should_be_equal_to_more_then_two_lower_boundary() \
        -> None:
    cat_age = 28
    dog_age = 29
    assert get_human_age(cat_age, dog_age) == [3, 3]


def test_get_human_age_should_be_equal_to_more_then_two() -> None:
    cat_age = 100
    dog_age = 100
    assert get_human_age(cat_age, dog_age) == [21, 17]
