from test_api.checks import run_test, skip_test, format_err_msg

# This function should take a string representing a time with hours and
#  minutes separated by a colon e.g. "13:25"
# Some of the times are written in the 24-hour clock format
# This function should return the time written in the 12-hour clock format


def convert_time_string(sample_string):
    hour=0
    hour_string=sample_string[:2]
    if int(hour_string) > 12:
        hour=int(hour_string) - 12
        return '0'+str(hour)+':'+sample_string[3:]
    elif hour_string=='00':
        return '12'+':'+sample_string[3:]
    else:
        return sample_string
    pass


@run_test
def test_convert_time_string_returns_the_string_unchanged_if_already_within_the_right_format():
    assert convert_time_string("06:28") == "06:28", \
        format_err_msg("06:28", convert_time_string("06:28"))


@run_test
def test_convert_time_string_converts_an_afternoon_time_to_the_12_hour_format():
    assert convert_time_string("16:07") == "04:07", \
        format_err_msg("04:07", convert_time_string("16:07"))


@run_test
def test_convert_time_string_converts_times_in_the_hour_after_midnight_to_the_12_hour_format():
    assert convert_time_string("00:56") == "12:56", \
        format_err_msg("12:56", convert_time_string("00:56"))
    assert convert_time_string("00:00") == "12:00", \
        format_err_msg("12:00", convert_time_string("00:00"))


if __name__ == "__main__":
    test_convert_time_string_returns_the_string_unchanged_if_already_within_the_right_format()
    test_convert_time_string_converts_an_afternoon_time_to_the_12_hour_format()
    test_convert_time_string_converts_times_in_the_hour_after_midnight_to_the_12_hour_format()
