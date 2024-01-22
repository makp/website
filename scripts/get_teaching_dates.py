"""Return teaching dates for building course schedule."""

from datetime import datetime, timedelta
import os


DATE_FORMAT = '%m-%d-%y'


def list_dates(first, last, no_class=[], weekdays=[0, 2]):
    """
    Return list of teaching dates.

    The list of dates are between `first` and `last`, and fall on
    specified `weekdays`.

    :param first: Start date as a string in 'mm-dd-yy' format.
    :param last: End date as a string in 'mm-dd-yy' format.
    :param no_class: Dates when there are no classes.
    :param weekdays: A list of integers representing weekdays where
    Monday is 0 and Sunday is 6.

    :return: A list of dates in 'mm-dd-yy' format. Days in `no_class`
    are marked with an asterisk.
    """
    # Convert str to datetime objects
    start_date = datetime.strptime(first, DATE_FORMAT)
    end_date = datetime.strptime(last, DATE_FORMAT)
    no_class_dates = {datetime.strptime(d, DATE_FORMAT) for d in no_class}

    lst_days = []

    current_day = start_date
    while current_day <= end_date:
        if current_day.weekday() in weekdays:
            day_str = current_day.strftime(DATE_FORMAT)
            if current_day in no_class_dates:
                lst_days.append(day_str + "*")
            else:
                lst_days.append(day_str)
        current_day += timedelta(days=1)

    return lst_days


def generate_filename(lst, output_dir):
    """
    Return filename based on class semester and year.

    :param lst: A list of dates.
    :param output_dir: The directory where `lst` will be saved.

    :return: A string representing the filename.
    """
    if not lst:
        raise ValueError("Empty list!")

    first_date = datetime.strptime(lst[0], DATE_FORMAT)
    first_month = first_date.strftime('%m')
    year = first_date.strftime('%y')

    terms = {'08': 'Fall', '01': 'Spring', '02': 'Spring'}

    term = terms.get(first_month)
    if not term:
        raise ValueError(f"Unknown term for month: {first_month}")

    file_name = f"teachingDates{term}{year}.txt"

    return os.path.join(output_dir, file_name)


def save_dates(lst, output_dir="."):
    """Write list of dates to a file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = generate_filename(lst, output_dir)
    with open(file_name, 'w') as f:
        f.write(', '.join(lst))
