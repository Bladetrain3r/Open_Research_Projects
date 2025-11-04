# Tests Directory

This directory contains automated tests for research scripts.

## Current Tests

- **test_analysis.py**: Tests for analysis.py functions
- **test_simulation.py**: Tests for simulation.py functions

## Running Tests

Run all tests:
```bash
python -m unittest discover TESTS
```

Run specific test file:
```bash
python -m unittest TESTS.test_analysis
```

Run individual test:
```bash
python TESTS/test_analysis.py
```

## Writing Tests

### Test Structure

1. Import unittest and the module to test
2. Create a test class inheriting from unittest.TestCase
3. Write test methods starting with `test_`
4. Use assertion methods to verify behavior

### Example

```python
import unittest
from SCRIPTS.my_script import my_function

class TestMyFunction(unittest.TestCase):
    def test_basic_case(self):
        result = my_function(input_data)
        self.assertEqual(result, expected_output)
```

## Best Practices

1. **Coverage**: Test both normal and edge cases
2. **Independence**: Tests should not depend on each other
3. **Clarity**: Use descriptive test names
4. **Speed**: Keep tests fast and focused
5. **Documentation**: Add docstrings to test classes and methods

## Test Guidelines

- Test each function's expected behavior
- Test error handling and edge cases
- Test with various input types and sizes
- Mock external dependencies when needed
- Keep tests maintainable and readable

## Continuous Integration

Tests should:
- Pass before merging pull requests
- Run automatically on commits
- Cover new functionality
- Maintain or improve coverage
