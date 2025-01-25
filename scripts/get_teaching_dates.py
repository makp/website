#!/usr/bin/env python3

"""Return teaching dates for building course schedule."""

import argparse
import os
from datetime import datetime, timedelta

DATE_FORMAT = "%m-%d-%y"


def list_dates(
    first: str,
    last: str,
    no_class: list | None,
    weekdays: tuple[int, int] = (0, 2),
) -> list[str]:
    """
    Return list of teaching dates.

    The list of dates are between `first` and `last`, and fall on specified
    `weekdays`. The `weekdays` parameter is a tuple of integers where Monday is
    0 and Sunday is 6. Dates in `no_class` are marked with an asterisk.
    """
    start_date = datetime.strptime(first, DATE_FORMAT)
    end_date = datetime.strptime(last, DATE_FORMAT)
    no_class_dates = frozenset(
        datetime.strptime(d, DATE_FORMAT) for d in (no_class or [])
    )

    dates = []
    current_day = start_date
    delta = timedelta(days=1)

    while current_day <= end_date:
        if current_day.weekday() in weekdays:
            day_str = current_day.strftime(DATE_FORMAT)
            dates.append(f"{day_str}*" if current_day in no_class_dates else day_str)
        current_day += delta

    return dates


def generate_filename(first_day: str, relative_dir: str) -> str:
    """Create filename and save it to the specified path."""
    date = datetime.strptime(first_day, DATE_FORMAT)

    month, year = (date.strftime(fmt) for fmt in ("%m", "%y"))

    terms = {
        "08": "Fall",
        "09": "Fall",
        "01": "Spring",
        "02": "Spring",
    }

    term = terms.get(month)
    if not term:
        raise ValueError(f"Unknown month value: {month}")

    file_name = f"teachingDates{term}{year}.txt"
    return os.path.join(os.path.abspath(relative_dir), file_name)


def create_and_save_dates(
    first: str,
    last: str,
    no_class: list | None,
    dir_out: str,
) -> None:
    dates = list_dates(first, last, no_class)
    filename = generate_filename(first, dir_out)
    with open(filename, "w") as f:
        f.write(", ".join(dates))
    print(f"Saved dates to {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate teaching dates")
    parser.add_argument("first", type=str, help="First day of class (mm-dd-yy)")
    parser.add_argument("last", type=str, help="Last day of class (mm-dd-yy)")
    parser.add_argument(
        "-n",
        "--no_class",
        nargs="*",
        type=str,
        help="Dates with no class (mm-dd-yy)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=".",
        help="Directory to save file (default: current)",
    )

    args = parser.parse_args()
    create_and_save_dates(args.first, args.last, args.no_class, args.output)
