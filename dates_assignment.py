import argparse
from datetime import datetime, timedelta
from calendar import monthcalendar, SATURDAY


def dates_bwn_two_dates_inclusive(start_date, end_date):
    for n in range(int((end_date - start_date).days + 1)):
        yield start_date + timedelta(n)


def check_fourth_saturday(dt):
    '''
    first week to be check for saturday
    if in first week pick fourth week  saturday
    else pick fifth week saturday
    '''

    calendar_month_lists = monthcalendar(dt.year, dt.month)
    first_week = calendar_month_lists[0]
    fourth_week = calendar_month_lists[3]
    if first_week[SATURDAY]:
        fourth_saturday = fourth_week[SATURDAY]
    else:
        fifth_week = calendar_month_lists[4]
        fourth_saturday = fifth_week[SATURDAY]
    return fourth_saturday == dt.day


def get_interval_dates(start_date_str, end_date_str):
    start_datetime = datetime.strptime(start_date_str, '%Y%m%d')
    end_datetime = datetime.strptime(end_date_str, '%Y%m%d')
    for dt in dates_bwn_two_dates_inclusive(start_datetime, end_datetime):
        if dt.isoweekday() == 6:
            if check_fourth_saturday(dt) and dt.day % 5 != 0:
                print(dt.strftime('%Y%m%d'))
            if not check_fourth_saturday(dt) and dt.day % 5 == 0:
                print(dt.strftime('%Y%m%d'))


def process_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('start_date',type=str, help='an string value for the start date')
    parser.add_argument('end_date', type=str, help='an string value for end date')
    args = parser.parse_args()
    return args.start_date,args.end_date


def execute():
    start_date, end_date = process_args()
    get_interval_dates(start_date,end_date)


if __name__ == '__main__':
    """
    >>> python dates_assignment.py 20180728 20180927
    """
    execute()
