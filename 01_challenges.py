from test_api.checks import run_test, skip_test, format_err_msg

# QUESTION 1
# This function should take 2 strings and join them together with a space
#  in between.
# return this newly created string


def connect_strings(word1, word2):
    return word1 + ' ' + word2
    


@run_test
def test_connect_strings():
    assert connect_strings("hello", "world") == "hello world", \
        format_err_msg("hello world", connect_strings("hello", "world"))
    assert connect_strings("cat", "hoang") == "cat hoang", \
        format_err_msg("cat hoang", connect_strings("cat", "hoang"))
    assert connect_strings("blue", "sky") == "blue sky", \
        format_err_msg("blue sky", connect_strings("blue", "sky"))


# QUESTION 2
# This function should take a string as an argument and return a boolean
#  based on whether the word given ends with 'ing'

def check_word_ends_with_ing(word):
    return word.endswith('ing') 
    


@run_test
def test_check_word_ends_with_ing():
    assert check_word_ends_with_ing("doing") is True, \
        format_err_msg(True, check_word_ends_with_ing("doing"))
    assert check_word_ends_with_ing("eating") is True, \
        format_err_msg(True, check_word_ends_with_ing("eating"))
    assert check_word_ends_with_ing("cry") is False, \
        format_err_msg(False, check_word_ends_with_ing("cry"))
    assert check_word_ends_with_ing("coder") is False, \
        format_err_msg(False, check_word_ends_with_ing("coder"))


# QUESTION 3
# This function should take a string as an argument
# each string may end with a full-stop, exclamation mark, or question mark
# if the string doesn't end with punctuation, return the string with a
#  full-stop added at the end. Otherwise, return the string unchanged

def add_missing_punctuation(word):
    if word.endswith(('.', '!', '?')):
        return word
    return word + '.'
    


@run_test
def test_add_missing_punctuation():
    assert add_missing_punctuation("Hello there!") == "Hello there!", \
        format_err_msg("Hello there!", add_missing_punctuation("Hello there!"))
    assert add_missing_punctuation("How's it going?") == "How's it going?", \
        format_err_msg("How's it going?",
                       add_missing_punctuation("How's it going?"))
    assert add_missing_punctuation("Yeah I'm good") == "Yeah I'm good.", \
        format_err_msg("Yeah I'm good.",
                       add_missing_punctuation("Yeah I'm good"))
    assert add_missing_punctuation("Nice") == "Nice.", \
        format_err_msg("Nice.", add_missing_punctuation("Nice"))


# QUESTION 4
# This function should take two arguments a and b, and return the remainder
#  of the division of a / b

def get_remainder(a,b):
    return a % b
    


@run_test
def test_get_remainder():
    assert get_remainder(10, 2) == 0, format_err_msg(0, get_remainder(10, 2))
    assert get_remainder(119, 10) == 9, \
        format_err_msg(9, get_remainder(119, 10))
    assert get_remainder(50, 6) == 2, format_err_msg(2, get_remainder(50, 6))


# QUESTION 5
# This function should take a dictionary and a key as its arguments and
#  return the value found at the provided key in the input dictionary
# If the key doesn't exist on the dictionary, this function should return a
#  string of "property not found"

def access_object(obj, key):
    value = obj.get(key)
    if value:
        return value
    return 'property not found'
    


@run_test
def test_access_object():
    assert access_object({"name": "nara", "age": 5}, "name") == "nara", \
        format_err_msg("nara", access_object(
            {"name": "nara", "age": 5}, "name"))
    assert access_object({"name": "nara", "age": 5}, "age") == 5, \
        format_err_msg(5, access_object({"name": "nara", "age": 5}, "age"))
    assert access_object({"name": "nara", "age": 5},
                         "email") == "property not found", \
        format_err_msg("property not found", access_object(
            {"name": "nara", "age": 5}, "email"))


# QUESTION 6
# In markdown files (e.g. 'README.md') we can denote words as bold by putting
#  two asterisks on either side of them, such as: **hello**
# This function should take a list of strings as an argument and return an
#  list consisting of the same strings but in bold - ie with two asterisks
#  either side of them

def make_all_words_bold(str_list):
    
    return ['**'+word+'**' for word in str_list]

@run_test
def test_make_all_words_bold():
    assert make_all_words_bold(["hello", "there", "world"]) == [
        "**hello**", "**there**", "**world**"], \
        format_err_msg(
        ["**hello**", "**there**", "**world**"],
        make_all_words_bold(["hello", "there", "world"]))


# QUESTION 7
# This function should take a list of numbers as an argument and return an
#  list containing all positive numbers from the input (retaining the order)
def get_positive_numbers(num_list):
    
    return [number for number in num_list if number >= 0]
    


@run_test
def test_get_positive_numbers():
    assert get_positive_numbers([1, -1, 2, -2, 3, -3]) == [1, 2, 3], \
        format_err_msg([1, 2, 3], get_positive_numbers([1, -1, 2, -2, 3, -3]))
    assert get_positive_numbers([-80, 9, 100, 13, 20, -7]) == [9, 100, 13, 20], \
        format_err_msg([9, 100, 13, 20], get_positive_numbers(
            [-80, 9, 100, 13, 20, -7]))
    assert get_positive_numbers([-1, -50, -999]) == [], \
        format_err_msg([], get_positive_numbers([-1, -50, -999]))


if __name__ == "__main__":
    test_connect_strings()
    test_check_word_ends_with_ing()
    test_add_missing_punctuation()
    test_get_remainder()
    test_access_object()
    test_make_all_words_bold()
    test_get_positive_numbers()
