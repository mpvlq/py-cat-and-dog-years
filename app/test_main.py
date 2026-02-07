from app.main import get_human_age


def test_should_return_list() -> None:
    assert (
        type(get_human_age(25, 25)) == list
    ), "Function should return a list."


def test_should_return_list_with_2_params() -> None:
    assert (
        len(get_human_age(25, 25)) == 2
    ), "Function should return a list with 2 parameters."


def test_should_less_than_15_animal_years_equal_to_0_human_year() -> None:
    assert (
        get_human_age(11, 1) == [0, 0]
    ), "Less than 15 animal years should be equal to 0 human year."


def test_should_15_animal_years_equal_to_1_human_year() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "15 animal years should be equal to 1 human year."


def test_should_next_9_years_after_15_give_1_more_human_year() -> None:
    assert (
        get_human_age(24, 25) == [2, 2]
    ), "Next 9 years after 15 should be equal to 2 human years."


def test_should_give_1_more_human_year_after_every_4_cat_years() -> None:
    assert (
        get_human_age(28, 25) == [3, 2]
    ), "Every 4 years after 24 should add 1 extra human year."


def test_should_give_1_more_human_year_after_every_5_dog_years() -> None:
    assert (
        get_human_age(100, 100) == [21, 17]
    ), "Every 5 years after 24 should add 1 extra human year."
