from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import requests

from ics import Calendar, Event

from src.libs.secrets_manager import get_secret


url = get_secret('ICAL_URL')
calendar = None
calendar_reload_at = datetime.now()


def load_calendar() -> Calendar:
    return Calendar(requests.get(url).text)


def get_tasks() -> set[Event]:
    global calendar, calendar_reload_at
    if calendar is None or calendar_reload_at < datetime.now():
        calendar = load_calendar()
        calendar_reload_at = datetime.now() + relativedelta(hours=1)

    return calendar.events


def get_tasks_as_df() -> pd.DataFrame:
    df_data = {
        'uid': [],
        'name': [],
        'begin': [],
        'end': [],
        'duration': [],
        'description': []
    }

    tasks = get_tasks()
    for task in tasks:
        df_data['uid'].append(task.uid)
        df_data['name'].append(task.name)
        df_data['begin'].append(task.begin.datetime)
        df_data['end'].append(task.end.datetime)
        df_data['duration'].append(task.duration)
        df_data['description'].append(task.description)

    df = pd.DataFrame(df_data).sort_values('begin').reset_index(drop=True)

    return df
