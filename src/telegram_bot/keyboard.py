from telegram import InlineKeyboardButton


keyboard_options = {
    'keyboard_main': 'На главную',
    'keyboard_motivation': 'Получить мотивацию',
    'keyboard_hide': 'Скрыть',
    'motivation_quote': 'Цитата',
    'motivation_advice': 'Совет',
    'motivation_exams': 'Перед экзаменом',
    'motivation_time-management': 'Тайм-менеджмент',
    'tasks_nearest': 'Посмотреть ближайшие задачи'
}


def get_keyboard_button(option: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(keyboard_options[option], callback_data=option)


keyboards = {
    'main': [
        [
            get_keyboard_button('keyboard_motivation')
        ],
        [
            get_keyboard_button('tasks_nearest')
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
            get_keyboard_button('keyboard_main')
        ],
        [
            get_keyboard_button('keyboard_hide')
        ]
    ]
}
