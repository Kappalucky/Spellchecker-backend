"""Core Common: Functions for use throughout the application"""

# Python imports
import re

# Django imports
from django.conf import settings

# 3rd party apps
# Local app imports
#* Dictionary file location
file_path = '%s/dictionary.txt' % (settings.STATIC_ROOT)

def init_dictionary(path):
	try:
		file = open(path, 'r')
		words = file.readlines()
		dictionary = [dict_word.strip() for dict_word in words]
		file.close()

		return dictionary
	except:
		raise Exception('Unable to open file')

def rule_checker(user_word):
	'''Check if letter in word repeats consecutively 3 or more times'''
	if len(re.findall(r'([a-zA-Z])\1{2,}', user_word, re.I)) != 0:
		raise Exception('Multiple characters present')

	'''check if islower/upper is true, return true'''
	if user_word.isupper() or user_word.islower():
		return True
	else:
		#* Mixed cased word will still be checked, missing vowels will be treated as misspelled word
		return False

def get_word(user_word):
	suggestions = []
	user_word_lower = user_word.lower()
	dictionary = init_dictionary(file_path)
	rule_checker_status = rule_checker(user_word)

	if rule_checker_status == True:
		if user_word_lower in dictionary:
			return {'correct': rule_checker_status, 'suggestions': suggestions}
		raise Exception('Word not in dictionary')
	else:
		if user_word_lower in dictionary:
			suggestions.append(user_word_lower)
		else:
			raise Exception('Word not in dictionary')

		#* check if other words in array that match word and not the same length, add to array
		for word in dictionary:
			if user_word_lower[:len(user_word_lower)] in word[:len(user_word_lower)] and len(user_word_lower) != len(word):
				suggestions.append(word)

		return {'correct': rule_checker_status, 'suggestions': suggestions}
