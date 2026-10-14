import pytest
from process import process


@pytest.mark.statement
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2], ["positivo", "par"]),
    ],
)
def test_statement_coverage(values, expected):
    assert process(values) == expected

 
@pytest.mark.branch
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2], ["positivo", "par"]),
        ([1], ["positivo"]),
        ([0], ["par"]),
        ([-1], []),
    ],
)
def test_branch_coverage(values, expected):
    assert process(values) == expected
    

@pytest.mark.path
@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, 2], ["positivo", "par", "positivo", "par"]),
        ([2, 1], ["positivo", "par", "positivo"]),
        ([2, 0], ["positivo", "par", "par"]),
        ([2, -1], ["positivo", "par"]),
        ([1, 2], ["positivo", "positivo", "par"]),
        ([1, 1], ["positivo", "positivo"]),
        ([1, 0], ["positivo", "par"]),
        ([1, -1], ["positivo"]),
        ([0, 2], ["par", "positivo", "par"]),
        ([0, 1], ["par", "positivo"]),
        ([0, 0], ["par", "par"]),
        ([0, -1], ["par"]),
        ([-1, 2], ["positivo", "par"]),
        ([-1, 1], ["positivo"]),
        ([-1, 0], ["par"]),
        ([-1, -1], []),
    ],
)
def test_path_coverage(values, expected):
    assert process(values) == expected