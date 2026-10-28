# Lab 5 — Static Code Analysis Issue Table

| Issue | Type | Description | Fix Approach |
|---|---|---|---|
| Unsafe eval() | Security | Could execute unwanted Python code. | Replaced eval() with regex validation. |
| Mutable default argument | Code quality | A list could be shared across function calls. | Changed the default to None. |
| Weak random generation | Security | Standard random generation was flagged. | Used secrets.randbelow(). |
| Silent exception handling | Code quality | Errors could be silently ignored. | Added explicit validation. |
| Missing docstrings | Code quality | Module and functions lacked documentation. | Added docstrings. |
| Unused imports | Style | Imported modules were not used. | Removed unused imports. |
| Unsafe file handling | Code quality | File handling lacked encoding and a context manager. | Used with open() and UTF-8 encoding. |
| Function naming | Style | Function name did not follow snake_case. | Renamed printSales() to print_sales(). |
| Formatting violations | Style | Whitespace and line-length issues existed. | Fixed formatting using Flake8. |
| Invalid input validation | Logic | Invalid quantities or tax rates could cause errors. | Added input validation. |

## Verification Results

- Pylint: 10.00/10
- Bandit: No issues identified
- Flake8: No reported violations