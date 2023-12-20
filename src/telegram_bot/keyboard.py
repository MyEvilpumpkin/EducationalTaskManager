"""
Telegram bot keyboards definition module
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message  # Required for keyboards management


async def keyboard(message: Message, keyboard_name: str) -> None:
    """
    Send keyboard
    """

    keyboard_ = keyboards[keyboard_name]
    await message.reply_text('Пожалуйста, выберите:', reply_markup=InlineKeyboardMarkup(keyboard_))


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
    'tasks_daily-update': 'Ежедневные сообщения о задачах\n(подписаться/отписаться)',
    'pomodoro_work': 'Работа (25 мин.)',
    'pomodoro_rest': 'Отдых (5 мин.)',
    'pomodoro_stop': 'Остановка таймера',
}


def _get_keyboard_button(option: str) -> InlineKeyboardButton:
    """
    Create keyboard button
    """

    return InlineKeyboardButton(keyboard_options[option], callback_data=option)


keyboards = {
    'main': [
        [
            _get_keyboard_button('keyboard_motivation')
        ],
        [
            # get_keyboard_button('keyboard_tasks')
            _get_keyboard_button('tasks_nearest')  # Temp
        ],
        [
            # get_keyboard_button('keyboard_tools')
            _get_keyboard_button('keyboard_pomodoro')  # Temp
        ],
        [
            _get_keyboard_button('keyboard_hide')
        ]
    ],
    'motivation': [
        [
            _get_keyboard_button('motivation_quote'),
            _get_keyboard_button('motivation_advice')
        ],
        [
            _get_keyboard_button('motivation_exams'),
            _get_keyboard_button('motivation_time-management')
        ],
        [
            _get_keyboard_button('keyboard_main'),
            _get_keyboard_button('keyboard_hide')
        ]
    ],
    'tasks': [
        [
            _get_keyboard_button('tasks_nearest')
        ],
        [
            _get_keyboard_button('tasks_daily-update')
        ],
        [
            _get_keyboard_button('keyboard_main'),
            _get_keyboard_button('keyboard_hide')
        ]
    ],
    'tools': [
        [
            _get_keyboard_button('keyboard_pomodoro')
        ],
        [
            _get_keyboard_button('keyboard_main'),
            _get_keyboard_button('keyboard_hide')
        ]
    ],
    'pomodoro': [
        [
            _get_keyboard_button('pomodoro_work'),
            _get_keyboard_button('pomodoro_rest')
        ],
        [
            _get_keyboard_button('pomodoro_stop')
        ],
        [
            # get_keyboard_button('keyboard_tools'),
            _get_keyboard_button('keyboard_main'),  # Temp
            _get_keyboard_button('keyboard_hide')
        ]
    ]
}
