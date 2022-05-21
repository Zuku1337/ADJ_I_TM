import re
import string


def remove_emoticons(text: str) -> str:
    return re.sub('[;:][\^s]', ' ', text)


def text_to_lower(text: str) -> str:
    return text.lower()


def remove_numbers(text: str) -> str:
    return re.sub('\d', ' ', text)


# Remove spaces both in the BEGINNING and in the END of a string
def remove_whitespaces(text: str) -> str:
    return text.strip()


def remove_punctuation(text: str) -> str:
    return re.sub(r'[^\w\s]', '', text)


def remove_single_apostrophes(text: str) -> str:
    return re.sub('(?<=[a-z])\'(?=[a-z])', ' ', text)


def remove_double_apostrophes(text: str) -> str:
    return re.sub("(?<=[a-z])'(?=[a-z])", ' ', text)
