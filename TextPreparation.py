import RegexHelper
import StopWordsHelper
import StemmingHelper
import WordsBagHelper


def regex_helper(text: list) -> str:
    x = []
    for word in text:
        if len(word) >= 3:
            word = RegexHelper.remove_emoticons(word)
            word = RegexHelper.remove_numbers(word)
            word = RegexHelper.text_to_lower(word)
            word = RegexHelper.remove_single_apostrophes(word)
            word = RegexHelper.remove_double_apostrophes(word)
            word = RegexHelper.remove_whitespaces(word)
            word = RegexHelper.remove_punctuation(word)
            x.append(word)
    return x


def stop_words_helper(text: str) -> list:
    return StopWordsHelper.stop_words(text)


def stemming_helper(text: str) -> list:
    return StemmingHelper.stemming(text)


def words_bag_helper(words: list) -> dict:
    return WordsBagHelper.words_bag(words)


def prepared_text(text: str) -> list:
    word = text.split()
    x = stemming_helper(stop_words_helper(regex_helper(word)))
    return x
