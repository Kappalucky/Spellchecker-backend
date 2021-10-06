"""Core Common: Functions for use throughout the application"""

# Python imports
import re

# Django imports
from django.conf import settings

# 3rd party apps
# Local app imports
#* Dictionary file location
file_path = '%s/dictionary.txt' % (settings.STATIC_ROOT)

def rule_checker(user_word):
	#* No repeated Characters
	'''Check if letter in word repeats consecutively 3 or more times'''
	regex = r'([a-zA-Z])\1{2,}'
	search = re.findall(regex, user_word, re.I)
	if len(search) != 0:
		print('Multiple characters present')
		raise Exception('Multiple characters present')

	#* lowercase or uppercase true
	'''check if islower/upper is true, return true'''
	if user_word.isupper() or user_word.islower():
		print('Word is either uppercase or lowercase')
		return True
	else:
		#* mixed case can still check for the word
		'''if other methods did not fail, continue/ return false'''
		print('Multicase')
		return False

	#* No missing vowels
	'''Check word against words without vowels, if match, return true. else return exception'''

def get_word(user_word):
	#* Check if list/hashtable is empty

	#* add words from dictionary to list/hastable if not in memory
	file = open(file_path, 'r')
	words = file.readlines()
	dictionary = [dict_word.strip() for dict_word in words]

	vowel_free_words = []
	suggestions = []

	#* check if word passes rule checker function
	if rule_checker(user_word):
		if user_word in dictionary:
			return {'correct': rule_checker(user_word), 'suggestions': suggestions}
		else:
			raise Exception('Word not in dictionary')
	else:
		#* change word to lowercase
		#* check list for word, if present add to array
		if user_word.lower() in dictionary:
			suggestions.append(user_word.lower())

		#* check if other words in array that match word and not the same length, add to array
		for word in dictionary:
			if user_word.lower() in word and len(user_word) != len(word):
				suggestions.append(word)
				print(suggestions)

		return {'correct': rule_checker(user_word), 'suggestions': suggestions}
