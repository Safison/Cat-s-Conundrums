from test_api.checks import run_test, skip_test, format_err_msg
import math 
# This function folds a list in the middle n number of times.

# If the list has a odd length, then fold on the middle index (the
#  middle number therefore won't change)
# other wise you fold in the 'gap' between the two middle integers and so
#  all integers are folded.

# To 'fold' the numbers add them together.

# For example:

# Fold 1-times:
# [1,2,3,4,5] -> [6,6,3]
# Here we fold the 1st with the last and the second with the 4th. As it is
#  odd in length, the middle index is not folded


def fold_list(list_to_fold, fold_count):
    # new_list = []
    # limit = len(list_to_fold) // 2
    # print(f'limit is {limit}')
    # firstcounter = 0
    # lastcounter = -1
    # fold_no = 0
    # i = 0
    # while fold_no < fold_count: 
    #     while i < limit:
    #         new_list.append(list_to_fold[i] + list_to_fold[lastcounter])
    #         firstcounter += 1
    #         lastcounter -= 1
    #         i += 1
    #     fold_count += 1
    # return new_list
    for _ in range (fold_count):
        length = len(list_to_fold)
        mid = length // 2
    
        if length <= 1:
            break
        if length % 2 == 0:
            list_to_fold=[list_to_fold[i] + list_to_fold[length -1 - i] for i in range(mid)]
        else:
            left=[list_to_fold[i] + list_to_fold[length -1 - i] for i in range(mid)]
            list_to_fold=left + [list_to_fold[mid]]
    return list_to_fold



    pass


@run_test
def test_fold_list_folds_an_even_length_list():
    assert fold_list([1, 2], 1) == [3], \
        format_err_msg([3], fold_list([1, 2], 1))
    assert fold_list([1, 2, 3, 10, 34, 100], 1) == [101, 36, 13], \
        format_err_msg([101, 36, 13], fold_list([1, 2, 3, 10, 34, 100], 1))


@run_test
def test_fold_list_folds_an_odd_length_list():
    assert fold_list([1, 2, 3], 1) == [4, 2], \
        format_err_msg([4, 2], fold_list([1, 2, 3], 1))


@run_test
def test_fold_list_folds_an_even_length_list_multiple_times():
    assert fold_list([1, 2, 3, 10, 34, 100], 2) == [114, 36], \
        format_err_msg([114, 36], fold_list([1, 2, 3, 10, 34, 100], 2))


@run_test
def test_fold_list_folds_a_list_to_a_single_value():
    assert fold_list([1, 2, 3, 10, 34, 100], 3) == [150], \
        format_err_msg([150], fold_list([1, 2, 3, 10, 34, 100], 3))


@run_test
def test_fold_list_returns_repeated_folds_remain_the_same():
    assert fold_list([1, 2, 3, 10, 34, 100], 4) == [150], \
        format_err_msg([150], fold_list([1, 2, 3, 10, 34, 100], 4))


if __name__ == "__main__":
    test_fold_list_folds_an_even_length_list()
    test_fold_list_folds_an_odd_length_list()
    test_fold_list_folds_an_even_length_list_multiple_times()
    test_fold_list_folds_a_list_to_a_single_value()
    test_fold_list_returns_repeated_folds_remain_the_same()
