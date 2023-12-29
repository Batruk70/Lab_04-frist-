import pytest
from libraly import calculator

def test_calculator():

    result1 = calculator(5, 2, "+")
    assert result1 == 7
    result2 = calculator(5, 2, "-")
    assert result2 == 3
    result3 = calculator(4, 3, "*")
    assert result3 == 12
    result4 = calculator(8, 2, "/")
    assert result4 == 4

if __name__ == "__main__":
    pytest.main()
