"""
Module that contains code for getting tasks (events) from the calendar
"""

from datetime import datetime, timedelta  # Required for calendar caching time management
import requests                           # Required for calendar downloading
from ics import Calendar, Event           # Required for calendar data representation
import pandas as pd                       # Required for another calendar data representation

from configuration.secrets import get_secret    # Required to get secrets
from configuration.settings import get_setting  # Required to get settings


calendar_url = get_secret('CALENDAR_URL')
calendar_tz = get_setting('CALENDAR_TZ')
calendar_cache = None
calendar_cache_reload_at = datetime.now()
calendar_cache_reload_delta = timedelta(minutes=int(get_setting('CALENDAR_CACHE_RELOAD_DELTA_MINUTES')))


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

    df = pd.DataFrame(
        {
            'uid': pd.Series(df_data['uid'], dtype='str'),
            'name': pd.Series(df_data['name'], dtype='str'),
            'begin': pd.Series(df_data['begin'], dtype='object'),
            'end': pd.Series(df_data['end'], dtype='object'),
            'duration': pd.Series(df_data['duration'], dtype='timedelta64[ns]'),
            'description': pd.Series(df_data['description'], dtype='str')
        }
    ).sort_values('begin').reset_index(drop=True)

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
