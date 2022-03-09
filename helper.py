import csv
import numpy as np
from datetime import datetime, date, timedelta


def read_csv_datetime(path: str, date_conversion: str) -> (np.ndarray, np.ndarray):
    """
    Reads a CSV file with two columns: date, value
    :param path: file path to CSV
    :param date_conversion: either "date" or "weekday"
    :return: tuple of numpy arrays consisting of dates and values
    """
    date_, value = [], []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        if date_conversion == "date":
            for row in reader:
                date_.append(convert_date(row[0]))
                value.append(row[1])
        elif date_conversion == "weekday":
            for row in reader:
                date_.append(convert_weekday(row[0]))
                value.append(row[1])
        else:
            print("Invalid date conversion")
            exit(1)

    if date_conversion == "weekyear" or date_conversion == "weekday":
        return np.array(date_).astype(str), np.array(value).astype(int)

    return np.array(date_), np.array(value).astype(int)


def read_csv_status(path: str) -> (np.ndarray, np.ndarray):
    """
    Read a CSV file with two columns: user status, value
    :param path: file path to CSV
    :return: tuple of numpy arrays consisting of user status and values
    """
    status, value = [], []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        for row in reader:
            status.append(row[0].strip())
            value.append(row[1])

    return np.array(status).astype(str), np.array(value).astype(int)


def convert_date(date_: str) -> datetime:
    """
    Converts a string in format "YYYY-MM-dd" to a datetime object
    """
    dt = datetime.strptime(date_.strip(), '%Y-%m-%d')
    return date(dt.year, dt.month, dt.day)


def convert_weekday(n: str) -> str:
    """
    Converts number to weekday name.
    :param n: a number between 0 und 6
    :return: the (n+1)th weekday name
    """
    days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    return days[int(n)]


def merge_values(all_dates: [], dates: [], values: [], filler: str) -> []:
    """
    Extends `values` array according to `all_dates`.
    :param all_dates: 1d array
    :param dates: 2d array
    :param values: 2d array
    :param filler: specifies new values. Either "nan" or "zero"
    :return:
    """
    # allocate new 2d array for values
    new_values = [None] * len(values)
    if filler == "nan":
        for i in range(0, len(new_values)):
            new_values[i] = [np.NAN] * len(all_dates)
    elif filler == "zero":
        for i in range(0, len(new_values)):
            new_values[i] = [0] * len(all_dates)

    # if existing, fill new_values with actual values
    for v in range(0, len(values)):
        for d in range(0, len(all_dates)):
            j = np.where(dates[v] == all_dates[d])[0]
            if len(j) > 0:
                value = values[v][j]
                new_values[v][d] = value[0]
    return new_values


def create_all_dates(date_arr_to_merge: []) -> []:
    """
    Inserts missing dates into `date_arr_to_merge`
    :param date_arr_to_merge: 2d array
    """
    # merge and clean arrays
    dates = []
    for d in date_arr_to_merge:
        dates = np.append(dates, d)
    dates = np.unique(np.sort(dates))
    missing_dates = []

    # add missing dates
    i = 0
    while i < len(dates) - 1:
        j = i + 1
        diff = -1 * (dates[i] - dates[j]).days
        if diff > 1:
            for k in range(1, diff):
                new_d = dates[i] + timedelta(days=k)
                missing_dates = np.append(missing_dates, [new_d])
        i += 1
    dates = np.sort(np.append(dates, missing_dates))
    return dates
