from telegram import InlineKeyboardButton


keyboard_options = {
    'keyboard_hide': 'Скрыть',
    'keyboard_main': 'Главная',
    'keyboard_motivation': 'Мотивация',
    'keyboard_tasks': 'Задачи',
    'keyboard_tools': 'Инструменты',
    'keyboard_pomodoro': 'Помодоро',
    'motivation_quote': 'Цитата',
    'motivation_advice': 'Совет',
    'motivation_exams': 'Перед экзаменом',
    'motivation_time-management': 'Тайм-менеджмент',
    'tasks_nearest': 'Посмотреть ближайшие задачи',
    'pomodoro_work': 'Работа (25 мин.)',
    'pomodoro_rest': 'Отдых (5 мин.)',
    'pomodoro_stop': 'Остановка таймера',
}


def get_keyboard_button(option: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(keyboard_options[option], callback_data=option)


keyboards = {
    'main': [
        [
            get_keyboard_button('keyboard_motivation')
        ],
        [
            get_keyboard_button('keyboard_tasks')
        ],
        [
            get_keyboard_button('keyboard_tools')
        ],
        [
            get_keyboard_button('keyboard_hide')
        ]
    ],
    'motivation': [
        [
            get_keyboard_button('motivation_quote'),
            get_keyboard_button('motivation_advice')
        ],
        [
            get_keyboard_button('motivation_exams'),
            get_keyboard_button('motivation_time-management')
        ],
        [
            get_keyboard_button('keyboard_main'),
            get_keyboard_button('keyboard_hide')
        ]
    ],
    'tasks': [
        [
            get_keyboard_button('tasks_nearest')
        ],
        [
            get_keyboard_button('keyboard_main'),
            get_keyboard_button('keyboard_hide')
        ]
    ],
    'tools': [
        [
            get_keyboard_button('keyboard_pomodoro')
        ],
        [
            get_keyboard_button('keyboard_main'),
            get_keyboard_button('keyboard_hide')
        ]
    ],
    'pomodoro': [
        [
            get_keyboard_button('pomodoro_work'),
            get_keyboard_button('pomodoro_rest')
        ],
        [
            get_keyboard_button('pomodoro_stop')
        ],
        [
            get_keyboard_button('keyboard_tools'),
            get_keyboard_button('keyboard_hide')
        ]
    ]
}
