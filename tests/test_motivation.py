from providers.motivation import get_motivation


def test_get_motivation():
    prompt_text = "Нужна мотивация для выполнения домашнего задания"

    # Вызываем функцию и проверяем результат
    result = get_motivation(prompt_text)

    # Предполагаем, что результат не пустой (вы можете настроить свои ожидания)
    assert result.strip() != ""
