from test_api.checks import run_test, skip_test, format_err_msg

# Implement a function collect_like_terms which takes an expression in a
#  string like 'a + a + a' and then returns a string with a simplified
#  algebraic expression, which in the previous case would be 3a.
# The characters should be in alphabetical order by default.
# You can assume that the only operation connecting the terms is addition.


def collect_like_terms(expr):
    count = 0 
    new_str = ''
    for i in range(len(expr)):
        if expr[i] == '+':
            letter1 = expr[i-2]
            letter2 = expr[i+2]
            if letter1 == letter2:
                count += 1
                new_str = str(count) + letter1
            else:
                new_str += expr[i]
    new_str.strip()
    return new_str 



    pass


@skip_test
def test_collect_like_terms_returns_a_letter_when_passed_an_expression_with_a_single_letter():
    assert collect_like_terms("a") == "a", \
        format_err_msg('a', collect_like_terms("a"))
    assert collect_like_terms("b") == "b", \
        format_err_msg('b', collect_like_terms("b"))


@skip_test
def test_collect_like_terms_returns_the_expression_if_it_is_already_simplified_and_not_starting_with_a_1():
    assert collect_like_terms("2a") == "2a", \
        format_err_msg('2a', collect_like_terms("2a"))
    assert collect_like_terms("3a") == "3a", \
        format_err_msg('3a', collect_like_terms("3a"))


@skip_test
def test_collect_like_terms_returns_just_the_letter_if_it_starts_with_a_1():
    assert collect_like_terms("1a") == "a", \
        format_err_msg('1a', collect_like_terms("1a"))
    assert collect_like_terms("1y") == "y", \
        format_err_msg('1y', collect_like_terms("1y"))


@skip_test
def test_collect_like_terms_can_simplify_two_duplicated_letters_added_together():
    assert collect_like_terms("a + a") == "2a", \
        format_err_msg('2a', collect_like_terms("a + a"))

    assert collect_like_terms("c + c") == "2c", \
        format_err_msg('2c', collect_like_terms("c + c"))


@skip_test
def test_collect_like_terms_can_simplify_multiple_duplicated_letters_added_together():
    assert collect_like_terms("a + a + a") == "3a", \
        format_err_msg('3a', collect_like_terms("a + a + a"))
    assert collect_like_terms("z + z + z + z") == "4z", \
        format_err_msg('4z', collect_like_terms("z + z + z + z"))


@skip_test
def test_collect_like_terms_can_simplify_two_distinct_letters_in_alphabetical_order():
    assert collect_like_terms("a + b") == "a + b", \
        format_err_msg('a + b', collect_like_terms('a + b'))
    assert collect_like_terms("b + a") == "a + b", \
        format_err_msg('a + b', collect_like_terms('b + a'))


@skip_test
def test_collect_like_terms_can_simplify_a_mix_of_distinct_and_duplicate_letters_being_added_together():
    assert collect_like_terms("a + b + b") == "a + 2b", \
        format_err_msg('a + 2b', collect_like_terms('a + b + b'))
    assert collect_like_terms("a + a + a + b") == "3a + b", \
        format_err_msg('3a + b', collect_like_terms('a + a + a + b'))


@skip_test
def test_collect_like_terms_can_simplify_multiple_distinct_terms():
    assert collect_like_terms("ab + ab") == "2ab", \
        format_err_msg('ab + ab', collect_like_terms('2ab'))
    assert collect_like_terms("ab + ab + ab") == "3ab", \
        format_err_msg('ab + ab + ab', collect_like_terms('3ab'))


if __name__ == "__main__":
    test_collect_like_terms_returns_a_letter_when_passed_an_expression_with_a_single_letter()
    test_collect_like_terms_returns_the_expression_if_it_is_already_simplified_and_not_starting_with_a_1()
    test_collect_like_terms_returns_just_the_letter_if_it_starts_with_a_1()
    test_collect_like_terms_can_simplify_two_duplicated_letters_added_together()
    test_collect_like_terms_can_simplify_multiple_duplicated_letters_added_together()
    test_collect_like_terms_can_simplify_two_distinct_letters_in_alphabetical_order()
    test_collect_like_terms_can_simplify_a_mix_of_distinct_and_duplicate_letters_being_added_together()
    test_collect_like_terms_can_simplify_multiple_distinct_terms()
