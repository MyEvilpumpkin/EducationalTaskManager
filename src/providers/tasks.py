"""
Tasks provider
"""

from pytz import timezone                 # Required for tasks timezone handling
from datetime import datetime, timedelta  # Required to check the relevance of tasks
import pandas as pd                       # Required for tasks representation

from .icalendar.tasks import get_tasks_as_df, calendar_tz  # Required for obtaining tasks


def get_all_tasks() -> pd.DataFrame:
    """
    Get all tasks
    :return: tasks
    """

    return get_tasks_as_df()


def get_relevant_tasks(tasks: pd.DataFrame = None, relevance_delta: timedelta = None) -> pd.DataFrame:
    """
    Get relevant tasks
    :param tasks: base tasks (optional)
    :param relevance_delta: time delta for tasks relevance (optional)
    :return: tasks
    """

    if tasks is None:
        tasks = get_all_tasks()

    now = datetime.now(timezone(calendar_tz))

    actual_mark = tasks['end'] >= now
    upcoming_mark = tasks['begin'] <= now + relevance_delta if relevance_delta else True
    return tasks[actual_mark & upcoming_mark].reset_index(drop=True)
