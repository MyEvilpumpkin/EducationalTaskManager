from telegram import InlineKeyboardButton


keyboard_options = {
    'motivation': 'Получить мотивацию',
    'motivation_phrase': 'Получить мотивационную фразу',
    'nearest_tasks': 'Посмотреть ближайшие задачи'
}


def get_keyboard_button(option: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(keyboard_options[option], callback_data=option)


keyboards = {
    'main': [
        [
            get_keyboard_button('motivation')
        ],
        [
            get_keyboard_button('motivation_phrase')
        ],
        [
            get_keyboard_button('nearest_tasks')
        ]
    ]
}
