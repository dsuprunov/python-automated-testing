from datetime import datetime


def concat(*args) -> str:
    return ' '.join(args)


def get_times_of_day() -> str:
    match datetime.now().hour:
        case x if 0 <= x < 6:
            return 'Night'
        case x if 6 <= x < 12:
            return 'Morning'
        case x if 12 <= x < 18:
            return 'Afternoon'

    return 'Evening'


def greeting() -> str:
    return concat('Good', get_times_of_day())
