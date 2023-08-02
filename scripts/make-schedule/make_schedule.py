from datetime import datetime, timedelta
import os


def list_all_dates(first, last, weekdays=[0, 2]):
    """
    Generate a list of dates between `first` and `last` that fall on
    specified `weekdays`.

    :param first: Start date as a string in 'mm-dd-yy' format.
    :param last: End date as a string in 'mm-dd-yy' format.
    :param weekdays: A list of integers representing weekdays where
    Monday is 0 and Sunday is 6.

    :return: A list of dates in 'mm-dd-yy' format.
    """
    # Convert str to datetime objects
    start_date = datetime.strptime(first, '%m-%d-%y')
    end_date = datetime.strptime(last, '%m-%d-%y')

    dates_in_range = [start_date + timedelta(days=x)
                      for x in range((end_date-start_date).days + 1)]
    list_days = [date for date in dates_in_range if date.weekday() in weekdays]
    list_days = sorted(list_days)

    return [date.strftime('%m-%d-%y') for date in list_days]


def file_name_to_export(lst, output_dir):
    """
    Generate a filename based on the first date in the list.

    :param lst: A list of dates.
    :param output_dir: The directory where the CSV file will be saved.

    :return: A string representing the filename.
    """
    first_date = datetime.strptime(lst[0], '%m-%d-%y')
    first_month = first_date.strftime('%m')
    year = first_date.strftime('%y')

    terms = {'08': 'Fall', '01': 'Spring', '02': 'Spring'}
    term = terms.get(first_month, '')

    file_name = "teachingDates" + term + year + ".csv"

    return os.path.join(output_dir, file_name)


def export_file(lst, output_dir="."):
    file_name = file_name_to_export(lst, output_dir)
    with open(file_name, 'w') as f:
        f.write(', '.join(lst))
