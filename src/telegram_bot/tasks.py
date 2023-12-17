from src.modules.tasks_handler import get_actual_tasks


def nearest(n: int = 5) -> str:
    actual_tasks = get_actual_tasks()
    tasks_info = ''
    i = 0
    for index, task in actual_tasks.iterrows():
        tasks_info += f'{i + 1}. {task["name"]} - {task["begin"].strftime("%d.%m.%Y %H:%M")}\n'
        i += 1
        if i >= n:
            break

    return tasks_info


tasks = {
    'nearest': nearest
}
