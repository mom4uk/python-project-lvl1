# -*- coding: utf-8 -*-

"""Brain gcd game functions."""

from brain_games.utils import get_random_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_greatest_common_divisor(first_value, second_value):
    """Generate greatest common divisor."""
    if first_value % second_value == 0:
        return second_value
    return get_greatest_common_divisor(second_value, first_value % second_value)


def gcd():
    """Generate question and correct answer."""
    first_value = get_random_number(0, 100)
    second_value = get_random_number(0, 100)
    question = f'{first_value} {second_value}'
    correct_answer = str(get_greatest_common_divisor(first_value, second_value))
    return (question, correct_answer)
