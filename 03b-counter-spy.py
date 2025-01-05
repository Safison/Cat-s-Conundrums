from test_api.checks import run_test, skip_test, format_err_msg

#  


def counter_spy(people):
    for name in people:
        if 's' in name.lower() or 'p' in name.lower() or 'y' in name.lower():
            people.remove(name)
    if len(people)>0:
        people.sort()
    return people 
    pass


@run_test
def test_counter_spy_returns_an_empty_list_if_the_only_person_is_a_spy():
    assert counter_spy(['Simon']) == [], format_err_msg(
        [], counter_spy(['Simon']))


@run_test
def test_counter_spy_returns_a_list_with_all_spies_removed():
    assert counter_spy(['Simon', 'Cat', 'Kyle']) == ['Cat'], \
        format_err_msg(['Cat'], counter_spy(['Simon', 'Cat', 'Kyle']))
    assert counter_spy(['Simon', 'Alex', 'Kyle', 'Cat', 'Chon', 'Danika']) == [
        'Alex', 'Cat', 'Chon', 'Danika'], \
        format_err_msg(['Alex', 'Cat', 'Chon', 'Danika'], counter_spy(
            ['Simon', 'Alex', 'Kyle', 'Cat', 'Chon', 'Danika']))


# EXTRA CREDIT:

# Also, our spy admin team have asked that the names come back in alphabetical
#  order, for spy filing purposes.
# So if you could do that you'd really be saving them a lot of work. Thanks.

@run_test
def test_counter_spy_returns_a_list_with_names_in_alphabetical_order():
    assert counter_spy(['Simon', 'Cat', 'Kyle', 'Danika', 'Alex', 'Chon']) == [
        'Alex', 'Cat', 'Chon', 'Danika'], \
        format_err_msg(['Alex', 'Cat', 'Chon', 'Danika'], counter_spy(
            ['Simon', 'Cat', 'Kyle', 'Danika', 'Alex', 'Chon']))


if __name__ == "__main__":
    test_counter_spy_returns_an_empty_list_if_the_only_person_is_a_spy()
    test_counter_spy_returns_a_list_with_all_spies_removed()
    test_counter_spy_returns_a_list_with_names_in_alphabetical_order()
