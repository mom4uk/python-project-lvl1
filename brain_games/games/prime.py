# -*- coding: utf-8 -*-

"""Brain prime game functions."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Check value on prime."""
    if number < 2 or not number % 2:
        return False
    counter = 3
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 2
    return True


def prime():
    """Generate question and correct answer."""
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return (str(question), correct_answer)
