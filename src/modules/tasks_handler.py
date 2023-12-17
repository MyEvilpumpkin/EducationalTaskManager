from datetime import datetime
import pandas as pd

from src.ical_tasks.tasks import get_tasks_as_df


def get_all_tasks() -> pd.DataFrame:
    return get_tasks_as_df()


def get_actual_tasks() -> pd.DataFrame:
    tasks = get_all_tasks()
    actual_mark = tasks['end'].dt.date >= datetime.now().date()
    return tasks[actual_mark].reset_index(drop=True)
