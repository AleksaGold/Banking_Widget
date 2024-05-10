from src.utils import reformat_the_date, disguise_number


def test_reformat_the_date():
    assert reformat_the_date([{"date": "2019-07-03T18:35:29.512364"}]) == [{"date": "03.07.2019"}]
    assert reformat_the_date([{"date": "2018-07-03T18:35:29.512364"}]) == [{"date": "03.07.2018"}]
    assert reformat_the_date([{"date": "1999-12-02T18:35:29.510064"}]) != [{"date": "07.07.1999"}]
    assert reformat_the_date([{"date": "2000-12-10T18:35:29.510064"}]) == [{"date": "10.12.2000"}]


def test_disguise_number():
    assert disguise_number([{"from": "Maestro 1596837868705199"}], "from") == [{"from": "Maestro 1596 83** **** 5199 "}]
    assert disguise_number([{"to": "Счет 35383033474447895560"}], "to") == [{"to": "Счет **5560 "}]
    assert disguise_number([{"to": "Счет 35383033474447895560"}], "from") != [{"to": "Счет **5560 "}]
    assert disguise_number([{}], "from") == [{"from": ""}]
