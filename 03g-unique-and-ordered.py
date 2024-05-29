from test_api.checks import run_test, skip_test, format_err_msg

# Implement a function which takes as an argument a sequence and returns a
#  list of items without any elements with the same value next to each other
#  and preserving the original order of elements.
# The function should be able to to work with both strings and lists, and
#  should return a list.


def unique_and_ordered(seq):
    pass


def test_unique_and_ordered_returns_unique_ordered_numbers_from_an_list():
    assert unique_and_ordered(
        [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 1, 1]) == [1, 2, 3, 1], \
        format_err_msg([1, 2, 3, 1], unique_and_ordered(
            [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 1, 1]))


@skip_test
def test_unique_and_ordered_returns_unique_ordered_letters_from_a_string():
    assert unique_and_ordered("nnoorrtthhccooddeerrss") == [
        "n", "o", "r", "t", "h", "c", "o", "d", "e", "r", "s"], \
        format_err_msg(["n", "o", "r", "t", "h", "c", "o", "d", "e", "r", "s"],
                       unique_and_ordered('nnoorrtthhccooddeerrss'))


@skip_test
def test_unique_and_ordered_is_case_sensitive_for_strings():
    assert unique_and_ordered("AaAAABBBCCCc") == \
        ["A", "a", "A", "B", "C", "c"], \
        format_err_msg(["A", "a", "A", "B", "C", "c"], "AaAAABBBCCCc")


if __name__ == "__main__":
    test_unique_and_ordered_returns_unique_ordered_numbers_from_an_list()
    test_unique_and_ordered_returns_unique_ordered_letters_from_a_string()
    test_unique_and_ordered_is_case_sensitive_for_strings()
