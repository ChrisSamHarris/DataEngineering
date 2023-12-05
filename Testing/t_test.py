# https://www.youtube.com/watch?v=mzlH8lp4ISA&ab_channel=anthonywritescode

import pytest
import t

@pytest.mark.parametrize(
    ('input_number', 'expected_result'),
    (
        (6, 36),
        (10., 100.),
    )
)

def test_square_params(input_number, expected_result):
    assert t.square(input_number) == expected_result

def test_square():
    assert t.square(5) == 25 
    
def test_square_float():
    assert t.square(3.) == 9.
    
class TestSquare:
    # Requires 'Test' in the class name 
    def test_square(self):
        assert t.square(3) == 9
    
    
# Run testing with 'pytest t_test.py' | '-V' for more verboe output, including test name 

