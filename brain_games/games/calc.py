# -*- coding: utf-8 -*-

"""Brain calc game functions."""

import operator
from random import choice, randint


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
    first_operand = randint(0, 100)
    second_operand = randint(0, 100)
    question = f'{first_operand} {random_operator} {second_operand}'
    correct_answer = operations[random_operator](first_operand, second_operand)
    return (question, str(correct_answer))
