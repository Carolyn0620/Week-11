
import pytest

import project_module # import project_module fron my_project file


def test_something(my_data):    # asset > e.g. password. True when it is 42, otherwise False.
    assert my_data == 42         # compare to my_data in confetest

@pytest.mark.parametrize("values,expected_results",[
    (
    [1,2,3,4,5,6],
    [3.0, 4.0],
    ),
    (
    [-1,-2,-3,-4,-5,-6],
    [-3.0, -4.0],
    ),
])
def test_rolling_average(values,expected_results):

    result = project_module.rolling_average(values, 5) 
    assert result == expected_results               # Check if my_data is equal to 42
