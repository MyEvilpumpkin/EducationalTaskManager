"""
Motivation tests
"""

from providers.motivation import get_motivation  # Required for testing the motivation feature


def test_get_motivation():
    """
    Base motivation test
    """

    prompt_text = 'Нужна мотивация для выполнения домашнего задания'

    result = get_motivation(prompt_text)

    assert result.strip() != ''
