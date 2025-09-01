import json
from datetime import date, timedelta


def get_calendar_week() -> int:
    return date.today().isocalendar()[1]

def get_today() -> str:
    return date.today().strftime("%d.%m.%Y")

def get_yesterday() -> str:
    return (date.today() - timedelta(1)).strftime("%d.%m.%Y")

def fetch_json(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as _:
        return json.load(_)
