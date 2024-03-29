import pytest
from datetime import datetime

from src.sample_package.sample_module import (
    concat,
    get_times_of_day,
    greeting
)


@pytest.mark.parametrize('test_input, expected', [
    (['a'], 'a'),
    (['a', 'b'], 'a b'),
])
def test_concat(test_input, expected):
    assert concat(*test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([1], '1'),
    (['a', 1], 'a 1'),
])
def test_concat_exception(test_input, expected):
    with pytest.raises(TypeError):
        concat(*test_input)


def time_of_day() -> list[tuple[datetime, str]]:
    return list(
        map(
            lambda x: (datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), x[1]),
            [
                ('2024-01-01 01:00:00', 'Night'),
                ('2024-01-01 08:00:00', 'Morning'),
                ('2024-01-01 14:00:00', 'Afternoon'),
                ('2024-01-01 20:00:00', 'Evening')
            ]
        )
    )


@pytest.mark.parametrize(
    'test_input, expected',
    time_of_day()
)
def test_get_time_of_day(mocker, test_input, expected):
    mock_now = mocker.patch('src.sample_package.sample_module.datetime')
    mock_now.now.return_value = test_input

    assert get_times_of_day() == expected


@pytest.mark.parametrize(
    'test_input, expected',
    map(lambda x: (x[0], concat('Good', x[1])), time_of_day())
)
def test_greeting(mocker, test_input, expected):
    mock_now = mocker.patch('src.sample_package.sample_module.datetime')
    mock_now.now.return_value = test_input

    assert greeting() == expected
