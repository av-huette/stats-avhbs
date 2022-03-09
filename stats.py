import os
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import matplotlib.dates as mdates
import numpy as np
import helper as h

dir_name, file_name = os.path.split(os.path.realpath(__file__))

"""
Warning: redundancy in plotting incoming
"""


def plot_item_types_line(year: str) -> None:
    """
    Plots a line chart of consumed items over time.
    """
    path_alc = f"{dir_name}/data/item_type/demo_alcoholic_sold_by_day_" + year + ".csv"
    path_non = f"{dir_name}/data/item_type/demo_non-alcoholic_sold_by_day_" + year + ".csv"
    path_foo = f"{dir_name}/data/item_type/demo_food_sold_by_day_" + year + ".csv"

    date_alc, alc = h.read_csv_datetime(path_alc, "date")
    date_non, non = h.read_csv_datetime(path_non, "date")
    date_foo, foo = h.read_csv_datetime(path_foo, "date")

    all_dates = h.create_all_dates([date_alc, date_non, date_foo])
    new_values = h.merge_values(all_dates, [date_alc, date_non, date_foo], [alc, non, foo], filler="zero")
    alc = new_values[0]
    non = new_values[1]
    foo = new_values[2]

    format_string = " Insg.: {0}\n Max.: {1}\nTag Ø: {2}"
    alc_text = format_string.format(np.sum(alc), np.max(alc), np.round(np.mean(alc), decimals=2))
    non_text = format_string.format(np.sum(non), np.max(non), np.round(np.mean(non), decimals=2))
    foo_text = format_string.format(np.sum(foo), np.max(foo), np.round(np.mean(foo), decimals=2))

    all_dates = date2num(all_dates)

    fig, (ax_alc, ax_non, ax_foo) = plt.subplots(3)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.subplots_adjust(hspace=0)

    ax_alc.set_title("Anzahl gebuchter Genussmittel " + year)
    ax_alc.axhline(y=np.mean(alc), color='#ffe5e5', linestyle='-')
    ax_alc.plot(all_dates, alc, label='Akloholisch', color='r')
    ax_alc.legend(loc="upper right")
    ax_alc.set_ylim(bottom=-1)
    ax_alc.xaxis_date()
    ax_alc.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax_alc.set_xlim(all_dates[0], all_dates[len(all_dates) - 1])
    ax_alc.grid(which='major', axis='x', linestyle='--')
    ax_alc.set(xticklabels=[])
    ax_alc.set_ylabel('Anzahl Genussmittel')
    plt.gcf().text(0.91, 0.75, alc_text, fontsize=10)

    ax_non.axhline(y=np.mean(non), color='#e8f1f7', linestyle='-')
    ax_non.plot(all_dates, non, label='Unalkoholisch', color='b')
    ax_non.legend(loc="upper right")
    ax_non.set_ylim(bottom=-1)
    ax_non.xaxis_date()
    ax_non.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax_non.set_xlim(all_dates[0], all_dates[len(all_dates) - 1])
    ax_non.grid(which='major', axis='x', linestyle='--')
    ax_non.set(xticklabels=[])
    ax_non.set_ylabel('Anzahl Genussmittel')
    plt.gcf().text(0.91, 0.5, non_text, fontsize=10)

    ax_foo.axhline(y=np.mean(foo), color='#e9f5e9', linestyle='-')
    ax_foo.plot(all_dates, foo, label='Essen', color='g')
    ax_foo.legend(loc="upper right")
    ax_foo.set_ylim(bottom=-0.3)
    ax_foo.xaxis_date()
    ax_foo.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax_foo.set_xlim(all_dates[0], all_dates[len(all_dates) - 1])
    ax_foo.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
    ax_foo.xaxis.set_tick_params(rotation=90)
    ax_foo.grid(which='major', axis='x', linestyle='--')
    ax_foo.set_xlabel('Montage')
    ax_foo.set_ylabel('Anzahl Genussmittel')
    plt.gcf().text(0.91, 0.25, foo_text, fontsize=10)

    plt.gcf().text(0.91, 0.11, "Summe: {0}".format(str(np.sum(alc) + np.sum(non) + np.sum(foo)), fontsize=10))

    plt.show()


def plot_item_types_bar(year: str) -> None:
    """
    Plots a line chart of consumed items over time.
    """
    path_alc = f"{dir_name}/data/item_type/demo_alcoholic_sold_by_day_" + year + ".csv"
    path_non = f"{dir_name}/data/item_type/demo_non-alcoholic_sold_by_day_" + year + ".csv"
    path_foo = f"{dir_name}/data/item_type/demo_food_sold_by_day_" + year + ".csv"

    date_alc, alc = h.read_csv_datetime(path_alc, "date")
    date_non, non = h.read_csv_datetime(path_non, "date")
    date_foo, foo = h.read_csv_datetime(path_foo, "date")

    all_dates = h.create_all_dates([date_alc, date_non, date_foo])
    new_values = h.merge_values(all_dates, [date_alc, date_non, date_foo], [alc, non, foo], filler="zero")
    alc = new_values[0]
    non = new_values[1]
    foo = new_values[2]

    format_string = " Insg.: {0}\n Max.: {1}\nTag Ø: {2}"
    alc_text = format_string.format(np.sum(alc), np.max(alc), np.round(np.mean(alc), decimals=2))
    non_text = format_string.format(np.sum(non), np.max(non), np.round(np.mean(non), decimals=2))
    foo_text = format_string.format(np.sum(foo), np.max(foo), np.round(np.mean(foo), decimals=2))

    all_dates = date2num(all_dates)

    fig, (ax_alc, ax_non, ax_foo) = plt.subplots(3)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.subplots_adjust(hspace=0)

    ax_alc.set_title("Anzahl gebuchter Genussmittel " + year)
    ax_alc.axhline(y=np.mean(alc), color='#ffe5e5', linestyle='-')
    ax_alc.bar(all_dates, alc, label='Akloholisch', color='r')
    ax_alc.legend(loc="upper left")
    ax_alc.set_ylim(bottom=0)
    ax_alc.xaxis_date()
    ax_alc.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax_alc.set_xlim(all_dates[0], all_dates[len(all_dates) - 1])
    ax_alc.grid(which='major', axis='x', linestyle='--')
    ax_alc.set(xticklabels=[])
    ax_alc.set_ylabel('Anzahl Genussmittel')
    plt.gcf().text(0.91, 0.75, alc_text, fontsize=10)

    ax_non.axhline(y=np.mean(non), color='#e8f1f7', linestyle='-')
    ax_non.bar(all_dates, non, label='Unalkoholisch', color='b')
    ax_non.legend(loc="upper left")
    ax_non.set_ylim(bottom=0)
    ax_non.xaxis_date()
    ax_non.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax_non.set_xlim(all_dates[0], all_dates[len(all_dates) - 1])
    ax_non.grid(which='major', axis='x', linestyle='--')
    ax_non.set(xticklabels=[])
    ax_non.set_ylabel('Anzahl Genussmittel')
    plt.gcf().text(0.91, 0.5, non_text, fontsize=10)

    ax_foo.axhline(y=np.mean(foo), color='#e9f5e9', linestyle='-')
    ax_foo.bar(all_dates, foo, label='Essen', color='g')
    ax_foo.legend(loc="upper left")
    ax_foo.set_ylim(bottom=-0)
    ax_foo.xaxis_date()
    ax_foo.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax_foo.set_xlim(all_dates[0], all_dates[len(all_dates) - 1])
    ax_foo.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
    ax_foo.xaxis.set_tick_params(rotation=90)
    ax_foo.grid(which='major', axis='x', linestyle='--')
    ax_foo.set_xlabel('Montage')
    ax_foo.set_ylabel('Anzahl Genussmittel')
    plt.gcf().text(0.91, 0.25, foo_text, fontsize=10)

    plt.gcf().text(0.91, 0.885, "Summe: {0}".format(str(np.sum(alc) + np.sum(non) + np.sum(foo)), fontsize=10))

    plt.show()


def plot_user_status_pie(year: str) -> None:
    """
    Plots a pie chart of bookings grouped by user status.
    """
    path = f"{dir_name}/data/user_status/demo_sold_items_total_by_status_" + year + ".csv"
    status, value = h.read_csv_status(path)
    colors = ["#4b92c3", "#ff983e", "#56b356", "#de5252", "#a985ca"]

    fig, ax = plt.subplots()
    ax.set_title("Buchungen nach Status " + year)
    ax.pie(value, labels=status, autopct='%1.0f%%', colors=colors)

    plt.show()


def plot_weekday_bar(year: str) -> None:
    """
    Plots a bar chart of total bookings grouped by weekday.
    """
    path = f"{dir_name}/data/sold_items/demo_sold_items_total_week_" + year + ".csv"
    weekday, value = h.read_csv_datetime(path, "weekday")
    percentage = ["{:.0%}".format(round(v / sum(value), 2)) for v in value]

    fig, ax = plt.subplots()
    ax.set_title("Buchungen an Wochentagen " + year)
    ax.bar(weekday, value, color="#99D4F4")
    ax.set_ylabel('Anzahl Buchungen')

    i = 0
    for p in ax.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        ax.annotate(percentage[i], (x + width / 2, y + height * 0.4), ha='center')
        i += 1

    plt.show()


def plot_item_types_pie(year: str) -> None:
    """
    Plots a pie chart of total bookings grouped by item type.
    """
    path_alc = f"{dir_name}/data/item_type/demo_alcoholic_sold_by_day_" + year + ".csv"
    path_non = f"{dir_name}/data/item_type/demo_non-alcoholic_sold_by_day_" + year + ".csv"
    path_foo = f"{dir_name}/data/item_type/demo_food_sold_by_day_" + year + ".csv"

    _, alc = h.read_csv_datetime(path_alc, "date")
    _, non = h.read_csv_datetime(path_non, "date")
    _, foo = h.read_csv_datetime(path_foo, "date")

    category = ["Alkoholisch", "Unhalkoholisch", "Essen"]
    values = [sum(alc), sum(non), sum(foo)]
    # colors = ["#FF4C4C", "#4C4CFF", "#4CA64C"]
    colors = ["#FF6666", "#6666FF", "#66B266"]

    fig, ax = plt.subplots()
    ax.set_title("Buchungen nach Genussmittel " + year)
    ax.pie(values, labels=category, autopct='%1.0f%%', colors=colors)

    plt.show()
