from test_api.checks import run_test, skip_test, format_err_msg

# This function takes a list of dictionaries and a string which should
#  match a key of the dictionaries in the list

# northcoders = [
#   { name: 'cat', location: 'manchester' },
#   { name: 'liam', location: 'york' },
#   { name: 'jim', location: 'leeds' },
#   { name: 'haz', location: 'manchester' },
#   { name: 'dave', location: 'leeds' },
# ];

# group_by(northcoders, 'location');

# The function returns a dictionary where the keys represent the matching
#  values and each matching dictionary is in a list.

#  // result

# {
#   manchester: [
#     { name: 'cat', location: 'manchester' },
#     { name: 'haz', location: 'manchester' },
#   ],
#   york: [
#     { name: 'liam', location: 'york' },
#   ],
#   leeds: [
#     { name: 'jim', location: 'leeds' },
#     { name: 'dave', location: 'leeds' },
#   ]
# }


def group_by(sample_list, key):
    pass


@run_test
def test_group_by_returns_northcoders_group_by_location():
    northcoders = [{"name": "cat", "location": "manchester"},
                   {"name": "liam", "location": "york"},
                   {"name": "jim", "location": "leeds"},
                   {"name": "haz", "location": "manchester"},
                   {"name": "dave", "location": "leeds"}]

    expected_grouped_data = {
        "manchester": [
            {"name": "cat", "location": "manchester"},
            {"name": "haz", "location": "manchester"}
        ],
        "york": [
            {"name": "liam", "location": "york"}
        ],
        "leeds": [
            {"name": "jim", "location": "leeds"},
            {"name": "dave", "location": "leeds"}
        ]
    }

    assert group_by(northcoders, "location") == expected_grouped_data


if __name__ == "__main__":
    test_group_by_returns_northcoders_group_by_location()
