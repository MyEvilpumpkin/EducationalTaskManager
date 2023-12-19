from datetime import datetime, timedelta
import pandas as pd

from ical_tasks.tasks import get_tasks_as_df


def get_all_tasks() -> pd.DataFrame:
    return get_tasks_as_df()


def get_actual_tasks(tasks: pd.DataFrame = None) -> pd.DataFrame:
    if tasks is None:
        tasks = get_all_tasks()
    actual_mark = tasks['end'].dt.date >= datetime.now().date()
    return tasks[actual_mark].reset_index(drop=True)


def get_upcoming_tasks(tasks: pd.DataFrame = None, delta: timedelta = None) -> pd.DataFrame:
    if tasks is None:
        tasks = get_all_tasks()
    actual_mark = tasks['end'].dt.date >= datetime.now().date()
    upcoming_mark = tasks['begin'].dt.date <= datetime.now().date() + delta if delta else True
    return tasks[actual_mark & upcoming_mark].reset_index(drop=True)
