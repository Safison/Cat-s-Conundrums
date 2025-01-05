from test_api.checks import run_test, skip_test, format_err_msg

# In this function, you need to find out which letter is missing. But you
#  can't use a reference lookup table (i.e. no list or dictionary with the
#  whole alphabet in it) so you will have think outside the box!
# This function needs to take a list and needs to return the letter it is
#  missing.
# You will always get a sorted list of consecutive letters, and it will
#  always have exactly one letter missing. The length of the list will always
#  be at least 2. The list will always contain letters in only one case.


def find_missing_letter(letters):
    str1=''
    case_char=letters[0]
    first_letter_index= ord(letters[0].lower()) - ord('a')+1
    i=1
    while i in range(len(letters)):
        if first_letter_index+i != ord(letters[i].lower()) - ord('a')+1:
            str1=first_letter_index+i
        i+=1
    if str1 != '':
        if letters[0]==letters[0].upper():
            return chr(int(str1) + ord('a')-1).upper()
        else:
            return chr(int(str1) + ord('a')-1)
    else:
        return str1
    pass


@run_test
def test_find_missing_letter_returns_an_empty_string_if_no_letters_are_missing():
    assert find_missing_letter(["A", "B", "C", "D", "E"]) == "", \
        format_err_msg('', find_missing_letter(["A", "B", "C", "D", "E"]))


@run_test
def test_find_missing_letter_returns_a_missing_capital_letter():
    assert find_missing_letter(["A", "B", "C", "E"]) == "D", \
        format_err_msg('D', find_missing_letter(["A", "B", "C", "E"]))


@run_test
def test_find_missing_letter_returns_a_missing_lower_case_letter():
    assert find_missing_letter(["e", "f", "g", "i"]) == "h", \
        format_err_msg('h', find_missing_letter(["e", "f", "g", "i"]))


if __name__ == "__main__":
    test_find_missing_letter_returns_an_empty_string_if_no_letters_are_missing()
    test_find_missing_letter_returns_a_missing_capital_letter()
    test_find_missing_letter_returns_a_missing_lower_case_letter()
