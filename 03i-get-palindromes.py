from test_api.checks import run_test, skip_test, format_err_msg

# This function takes a list of words and returns a list containing only
#  the palindromes.
# A palindrome is a word that is spelled the same way backwards.
# E.g. ['foo', 'racecar', 'pineapple', 'porcupine', 'tacocat'] =>
#  ['racecar', 'tacocat']


def get_palindromes(word_list):
    pass


@run_test
def test_get_palindromes_returns_empty_list_when_passed_empty_list():
    assert get_palindromes([]) == [], format_err_msg([], get_palindromes([]))


@skip_test
def test_get_palindromes_identifies_palindromes():
    assert get_palindromes(["racecar"]) == ["racecar"], \
        format_err_msg(["racecar"], get_palindromes(["racecar"]))
    assert get_palindromes(["racecar", "racecar"]) == ["racecar", "racecar"], \
        format_err_msg(["racecar", "racecar"],
                       get_palindromes(["racecar", "racecar"]))


@skip_test
def test_get_palindromes_ignores_non_palindromes():
    assert get_palindromes(["racecar", "kayak", "tacocat"]) == \
        ["racecar", "kayak", "tacocat"], \
        format_err_msg(["racecar", "kayak", "tacocat"],
                       get_palindromes(["racecar", "kayak", "tacocat"]))
    assert get_palindromes(["pineapple", "pony", "racecar"]) == ["racecar"], \
        format_err_msg(["pineapple", "pony", "racecar"],
                       get_palindromes(["racecar"]))


@skip_test
def test_get_palindromes_returns_empty_list_when_passed_no_palindromes():
    assert get_palindromes(["pineapple", "watermelon", "pony"]) == [], \
        format_err_msg([], get_palindromes(
            ["pineapple", "watermelon", "pony"]))


if __name__ == "__main__":
    test_get_palindromes_returns_empty_list_when_passed_empty_list()
    test_get_palindromes_identifies_palindromes()
    test_get_palindromes_ignores_non_palindromes()
    test_get_palindromes_returns_empty_list_when_passed_no_palindromes()
