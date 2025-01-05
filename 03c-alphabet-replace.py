from test_api.checks import run_test, skip_test, format_err_msg

# This function that accepts a string of any length, and replaces each letter
#  within each word with the corresponding index that that letter has in the
#  alphabet.
# You must have a space between each index number, and do NOT need to account
#  extra for spaces between words.


def alphabet_replace(sample_string):
    alpha_string=''
    for char in sample_string:
        if char.isalpha():
            alpha_index = str(ord(char.lower())-ord('a')+1)
            alpha_string += alpha_index + ' '
    alpha_string=alpha_string.strip()
    return alpha_string
    pass


@run_test
def test_alphabet_replace_returns_the_letters_in_a_single_word_with_codes():
    assert alphabet_replace("code") == "3 15 4 5", \
        format_err_msg("3 15 4 5", alphabet_replace("code"))


@run_test
def test_alphabet_replace_is_case_insensitive():
    assert alphabet_replace("Northcoders") == "14 15 18 20 8 3 15 4 5 18 19", \
        format_err_msg("14 15 18 20 8 3 15 4 5 18 19",
                       alphabet_replace("Northcoders"))


@run_test
def test_alphabet_replace_ignores_spaces_between_words():
    assert alphabet_replace("expert programming") == \
        "5 24 16 5 18 20 16 18 15 7 18 1 13 13 9 14 7", \
        format_err_msg("5 24 16 5 18 20 16 18 15 7 18 1 13 13 9 14 7",
                       alphabet_replace("expert programming"))


if __name__ == "__main__":
    test_alphabet_replace_returns_the_letters_in_a_single_word_with_codes()
    test_alphabet_replace_is_case_insensitive()
    test_alphabet_replace_ignores_spaces_between_words()
