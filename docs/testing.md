# Running Tests

This project uses pytest for unit testing.

## Installing pytest

```bash
python -m pip install pytest
```

## Running all tests

Run this from the project's root folder (not inside the tests/ folder):

```bash
python -m pytest
```

## What gets tested

- `tests/test_calculator.py` -> tests for calculator.py functions
- `tests/test_string_utils.py` -> tests for string_utils.py functions

## Continuous Integration

Tests also run automatically on GitHub via GitHub Actions every time code is
pushed or a pull request is opened. You can see the results under the
"Actions" tab of the repository.