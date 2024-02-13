import enum


class ActionAt(enum.Enum):
    sheet = "sheet"
    task = "task"


class Period(enum.Enum):
    week = "week"
    day = "day"


PERIOD_DAYS: dict = {
    Period.week: 7,
    Period.day: 1,
}
