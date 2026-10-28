# Lab 5: Static Code Analysis Report

## 1. Objective

The objective of this lab was to analyze and improve the quality, security, and formatting of a Python program using Pylint, Bandit, and Flake8.

## 2. Tools Used

- **Pylint:** Identifies code-quality problems and programming errors.
- **Bandit:** Detects potential security vulnerabilities in Python code.
- **Flake8:** Checks Python code style and formatting.

## 3. Issues Identified and Fixes Applied

The original program contained several code-quality and security issues.

| Issue | Fix Applied |
|---|---|
| Unsafe `eval()` | Replaced it with regular-expression validation. |
| Mutable default argument | Changed the default to `None`. |
| Weak random-number generation | Used `secrets.randbelow()`. |
| Missing docstrings | Added module and function documentation. |
| Unused imports | Removed unnecessary imports. |
| Unsafe file handling | Used a context manager and UTF-8 encoding. |
| Invalid function naming | Changed `printSales()` to `print_sales()`. |
| Formatting violations | Corrected formatting and whitespace. |
| Invalid input handling | Added validation for quantities and tax rates. |

## 4. Final Verification Results

- **Pylint:** 10.00/10.
- **Bandit:** No issues identified.
- **Flake8:** No reported violations.

The program was executed successfully after the fixes.

## 5. Conclusion

Static code analysis helped identify security, code-quality, and formatting problems in the retail point-of-sale program. The fixes improved code readability, input validation, file handling, and security. The final program passed the Pylint, Bandit, and Flake8 checks.
