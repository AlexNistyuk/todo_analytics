import enum


class Period(enum.Enum):
    week = "week"
    day = "day"


days_period_map: dict = {
    Period.week: 7,
    Period.day: 1,
}
