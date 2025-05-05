import pytest
from string_utils import StringUtils

utils = StringUtils()

# capitalize 
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello Moskow", "Hello Moskow"),
    ("123test", "123test")
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", " "),
    ("123", "123")
])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected

# trim 
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  test", "test"),
    ("  hello ", "hello "),
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) == expected

# contains 
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("Python", "P", True),
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
])
def test_contains_negative(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

# delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_string, char_to_remove, expected_output", [
    ('repository', 'r', 'epositoy'),
    ('long-term', '-', 'longterm'),
])
def test_delete_symbol_positive(input_string, char_to_remove, expected_output):
    assert utils.delete_symbol(input_string, char_to_remove) == expected_output

@pytest.mark.negative
@pytest.mark.parametrize("input_string, char_to_remove, expected_output", [
    ('test', 'z', 'test'),  # Символ отсутствует
    ('', 'a', ''),          # Пустая строка
])
def test_delete_symbol_negative(input_string, char_to_remove, expected_output):
    assert utils.delete_symbol(input_string, char_to_remove) == expected_output
