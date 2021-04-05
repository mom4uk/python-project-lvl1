# -*- coding: utf-8 -*-

"""Brain calc game functions."""

import operator
from random import choice

from brain_games.utils import get_random_number

DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_operator(coll):
    """Get random operator."""
    return choice(list(operations.keys()))


def calc():
    """Generate question and correct answer."""
    random_operator = get_operator(operations)
    first_operand = get_random_number(0, 100)
    second_operand = get_random_number(0, 100)
    question = f'{first_operand} {random_operator} {second_operand}'
    correct_answer = str(operations[operator](first_operand, second_operand))
    return (question, correct_answer)
