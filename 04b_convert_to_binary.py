from test_api.checks import run_test, skip_test, format_err_msg

# Implement a function which takes any decimal number and converts it into
#  binary format.
# The return value of the function should always be a string of "O"s and
#  "1"s representing the binary number


def convert_to_binary():
    pass


@run_test
def test_convert_to_binary_can_convert_a_single_digit_decimal_number_to_binary():
    assert convert_to_binary(0) == "0", \
        format_err_msg("0", convert_to_binary(0))
    assert convert_to_binary(1) == "1", \
        format_err_msg("1", convert_to_binary(1))
    assert convert_to_binary(2) == "10", \
        format_err_msg("10", convert_to_binary(2))
    assert convert_to_binary(3) == "11", \
        format_err_msg("11", convert_to_binary(3))
    assert convert_to_binary(4) == "100", \
        format_err_msg("100", convert_to_binary(4))
    assert convert_to_binary(5) == "101", \
        format_err_msg("101", convert_to_binary(5))
    assert convert_to_binary(6) == "110", \
        format_err_msg("110", convert_to_binary(6))
    assert convert_to_binary(7) == "111", \
        format_err_msg("111", convert_to_binary(7))


@skip_test
def test_convert_to_binary_can_convert_a_multiple_digit_decimal_number_to_binary():
    assert convert_to_binary(10) == "1010", \
        format_err_msg("1010", convert_to_binary(10))
    assert convert_to_binary(23) == "10111", \
        format_err_msg("10111", convert_to_binary(23))
    assert convert_to_binary(55) == "110111", \
        format_err_msg("110111", convert_to_binary(55))


if __name__ == "__main__":
    test_convert_to_binary_can_convert_a_single_digit_decimal_number_to_binary()
    test_convert_to_binary_can_convert_a_multiple_digit_decimal_number_to_binary()
