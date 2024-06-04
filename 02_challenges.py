from test_api.checks import run_test, skip_test, format_err_msg

# QUESTION 1
# This function should take two strings as arguments and return True if
#  their final character is the same or False if not


def check_same_final_character():
    pass


@run_test
def test_check_same_final_character():
    assert check_same_final_character("hello", "hello") is True, \
        format_err_msg(True, check_same_final_character("hello", "hello"))
    assert check_same_final_character("goodbye!", "goodbye?") is False, \
        format_err_msg(False, check_same_final_character(
            "goodbye!", "goodbye?"))


# QUESTION 2
# This function should take a string as an argument and return True if
#  every letter is upper case and False if at least one character is not

def is_all_upper_case():
    pass


@skip_test
def test_is_all_upper_case():
    assert is_all_upper_case("hello") is False, \
        format_err_msg(False, is_all_upper_case("hello"))
    assert is_all_upper_case("WORLD") is True, \
        format_err_msg(True, is_all_upper_case("WORLD"))
    assert is_all_upper_case("HI Mabel") is False, \
        format_err_msg(False, is_all_upper_case("HI Mabel"))


# QUESTION 3
# This function should take a string as its argument and return a
#  string consisting of all vowels found in the input (retaining the order)

def collect_the_vowels(str):
    pass


@skip_test
def test_collect_the_vowels():
    assert collect_the_vowels("a") == "a", \
        format_err_msg('a', collect_the_vowels("a"))
    assert collect_the_vowels("bcd") == "", \
        format_err_msg('', collect_the_vowels("bcd"))
    assert collect_the_vowels("bcdepiaouk") == "eiaou", \
        format_err_msg('eiaou', collect_the_vowels("bcdepiaouk"))


# QUESTION 4
# This function should take two arguments, a list and an index, and return
#  the element at that specified index

# The index provided may be equal to or greater than the length of the
#  given list. In this case, rather than counting past the end of the
#  list where there are no values, the indexing should be considered to
#  "loop back around" and continue from the start of the list

# For examples of this behaviour, look at the second group of tests below

def access_item(list, index):
    pass


@skip_test
def test_access_item_retrieves_item_when_passed_index_less_than_list_len():
    assert access_item(["a", "b", "c", "d"], 2) == "c", \
        format_err_msg("c", access_item(["a", "b", "c", "d"], 2))
    assert access_item(["a", "b", "c", "d"], 0) == "a", \
        format_err_msg("a", access_item(["a", "b", "c", "d"], 0))
    assert access_item(["a", "b", "c", "d"], 3) == "d", \
        format_err_msg("d", access_item(["a", "b", "c", "d"], 3))


@skip_test
def test_access_item_retrieves_item_when_passed_index_greater_or_equal_to_list_len():
    assert access_item(["a", "b", "c", "d"], 4) == "a", \
        format_err_msg("a", access_item(["a", "b", "c", "d"], 4))
    assert access_item(["a", "b", "c", "d"], 6) == "c", \
        format_err_msg("c", access_item(["a", "b", "c", "d"], 6))
    assert access_item(["a", "b", "c", "d"], 10) == "c", \
        format_err_msg("c", access_item(["a", "b", "c", "d"], 10))


# QUESTION 5
# This function should take a number from 1 to 7 inclusive, and return a
#  string of the corresponding day of the week
# BONUS POINTS: Try and solve this without using if statements! Hint: a
#  'lookup dictionary' might be useful here.

def find_day_of_the_week(num):
    pass


@skip_test
def test_find_day_of_the_week():
    assert find_day_of_the_week(3) == "Wednesday", \
        format_err_msg('Wednesday', find_day_of_the_week(3))
    assert find_day_of_the_week(7) == "Sunday", \
        format_err_msg('Sunday', find_day_of_the_week(7))
    assert find_day_of_the_week(1) == "Monday", \
        format_err_msg('Monday', find_day_of_the_week(1))


# QUESTION 6
# This function should take two numbers, a and b, and return a string
#  representing the value of a as a percentage of b

def create_percentage():
    pass


@skip_test
def test_create_percentage():
    assert create_percentage(1, 2) == "50%", \
        format_err_msg("50%", create_percentage(1, 2))
    assert create_percentage(50, 100) == "50%", \
        format_err_msg("50%", create_percentage(50, 100))
    assert create_percentage(2, 3) == "67%", \
        format_err_msg("67%", create_percentage(2, 3))
    assert create_percentage(3, 4) == "75%", \
        format_err_msg("75%", create_percentage(3, 4))
    assert create_percentage(1, 7) == "14%", \
        format_err_msg("14%", create_percentage(1, 7))


# QUESTION 7
# This function should take a string containing a number wrapped in a pair
#  of round brackets and return said number

def extract_number():
    pass


@skip_test
def test_extract_number():
    assert extract_number("lasjdasasj(1)asljdlajk") == 1, \
        format_err_msg(1, extract_number("lasjdasasj(1)asljdlajk"))
    assert extract_number("qwasdaoyer(666)iuwyeibasdahgsd") == 666, \
        format_err_msg(666, extract_number("qwasdaoyer(666)iuwyeibasdahgsd"))
    assert extract_number("qwasdasdfsyer(19827)iusdfsdfsd") == 19827, \
        format_err_msg(19827, extract_number("qwasdasdfsyer(19827)iusdfsdfsd"))
    assert extract_number("qwasdasdfsyer(5601)iusd5602sdfsd") == 5601, \
        format_err_msg(5601, extract_number(
            "qwasdasdfsyer(5601)iusd5602sdfsd"))
    assert extract_number("qwasdas27dfs28yer(29)ius3dfsdf0sd") == 29, \
        format_err_msg(29, extract_number("qwasdas27dfs28yer(29)ius3dfsdf0sd"))


if __name__ == "__main__":
    test_check_same_final_character()
    test_is_all_upper_case()
    test_collect_the_vowels()
    test_access_item_retrieves_item_when_passed_index_less_than_list_len()
    test_access_item_retrieves_item_when_passed_index_greater_or_equal_to_list_len()
    test_find_day_of_the_week()
    test_create_percentage()
    test_extract_number()
