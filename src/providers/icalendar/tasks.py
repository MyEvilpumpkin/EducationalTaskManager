"""
Module that contains code for getting tasks (events) from the calendar
"""

from datetime import datetime, timedelta  # Required for calendar caching time management
import requests                           # Required for calendar downloading
from ics import Calendar, Event           # Required for calendar data representation
import pandas as pd                       # Required for another calendar data representation

from configuration.secrets import get_secret  # Required to get the calendar url from secrets


calendar_url = get_secret('ICAL_URL')
calendar_cache = None
calendar_cache_reload_at = datetime.now()
calendar_cache_reload_delta = timedelta(hours=1)


def get_tasks_as_df() -> pd.DataFrame:
    """
    Get all tasks (events) from calendar as DataFrame
    :return: tasks in DataFrame format
    """

    df_data = {
        'uid': [],
        'name': [],
        'begin': [],
        'end': [],
        'duration': [],
        'description': []
    }

    tasks = _get_tasks()
    for task in tasks:
        df_data['uid'].append(task.uid)
        df_data['name'].append(task.name)
        df_data['begin'].append(task.begin.datetime)
        df_data['end'].append(task.end.datetime)
        df_data['duration'].append(task.duration)
        df_data['description'].append(task.description)

    df = pd.DataFrame(df_data).sort_values('begin').reset_index(drop=True)

    return df


def _get_tasks() -> set[Event]:
    """
    Get all tasks (events) from calendar
    :return: tasks
    """

    global calendar_cache, calendar_cache_reload_at

    if calendar_cache is None or calendar_cache_reload_at <= datetime.now():
        # Caching calendar
        calendar_cache = _load_calendar()
        calendar_cache_reload_at = datetime.now() + calendar_cache_reload_delta

    return calendar_cache.events


def _load_calendar() -> Calendar:
    """
    Calendar downloading
    :return: calendar
    """

    return Calendar(requests.get(calendar_url).text)
