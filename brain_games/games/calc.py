from brain_games.utils import get_random_number
from random import choice
import operator

DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
	}

def get_operator(coll):
	return choice(list(operations.keys()))

def calc():
	operator = get_operator(operations)
	first_operand = get_random_number()
	second_operand = get_random_number()
	question = "%d %s %d" % (first_operand, operator, second_operand)
	correct_answer = str(operations[operator](first_operand, second_operand))
	return (question, correct_answer)
