"""Core Common: Functions for use throughout the application"""

# Python imports
import re

# Django imports
from django.conf import settings

# 3rd party apps
# Local app imports

# * Dictionary file location
file_path = "%s/dictionary.txt" % (settings.STATIC_ROOT)


def init_data(path) -> list:
    try:
        file = open(path, "r")
        words = file.readlines()
        file.close()

        return words
    except:
        raise Exception("Unable to open file")


def init_hash_table(data) -> dict:
    table = {}

    for item in data:
        table[item.strip()] = True

    return table


def init_dictionary(data) -> list:
    return [word.strip() for word in data]


def hash_table_checker(table, word) -> bool:
    word_lower = word.lower()
    status = table.get(word_lower)

    if status is not None:
        return status
    else:
        return False


def dictionary_checker(dict, word) -> list:
    suggestions = []
    word_lower = word.lower()

    for dict_word in dict:
        if word_lower[: len(word_lower)] in dict_word[: len(word_lower)]:
            suggestions.append(dict_word)

    return suggestions


def rule_checker(word) -> bool:
    """Check if letter in word repeats consecutively 3 or more times"""
    if len(re.findall(r"([a-zA-Z])\1{2,}", word, re.I)) != 0:
        raise Exception("Multiple characters present")

    """check if islower/upper is true, return true"""
    if word.isupper() or word.islower():
        return True

    # * Mixed cased word will still be checked, missing vowels will be treated as misspelled word
    return False


def get_word(word) -> dict:
    dictionary = init_dictionary(init_data(file_path))
    hash_table = init_hash_table(dictionary)
    rule_checker_status = rule_checker(word)
    hash_status = hash_table_checker(hash_table, word)

    if rule_checker_status:  # * Rules passed
        if hash_status:
            return {"correct": hash_status, "suggestions": []}
        # * return words similar to passed word
        elif hash_status == False and len(dictionary_checker(dictionary, word)) != 0:
            return {
                "correct": hash_status,
                "suggestions": dictionary_checker(dictionary, word),
            }
        # * No word or words of similarity present
        raise Exception("Word not in dictionary")
    else:  # * A rule failed
        # * No words of similarity present
        if len(dictionary_checker(dictionary, word)) == 0:
            raise Exception("Word not in dictionary")
        # * return words similar to passed word
        return {
            "correct": rule_checker_status,
            "suggestions": dictionary_checker(dictionary, word),
        }
