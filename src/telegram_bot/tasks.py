from datetime import timedelta

import pandas as pd

from src.modules.tasks_handler import get_actual_tasks, get_upcoming_tasks


def nearest(n: int = 5) -> str:
    actual_tasks = get_actual_tasks()
    return get_tasks_info(actual_tasks, n)


tasks = {
    'nearest': nearest
}


def get_tasks_info(tasks_: pd.DataFrame, n: int = 0) -> str:
    tasks_info = ''

    i = 0
    for index, task in tasks_.iterrows():
        tasks_info += f'{i + 1}. {task["name"]} - {task["begin"].strftime("%d.%m.%Y %H:%M")}\n'
        i += 1

        if 0 < n <= i:
            break

    return tasks_info
