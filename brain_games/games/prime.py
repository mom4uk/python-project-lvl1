from brain_games.utils import get_random_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(value):
	if value < 2:
		return False
	i = 2
	while i <= value / 2:
		if value % i == 0:
			return False
		return True

def prime():
	question = get_random_number(1, 100)
	correct_answer = 'yes' if is_prime(question) == True else 'no'
	return (str(question), correct_answer)
