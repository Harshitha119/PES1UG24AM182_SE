# Lab 5: Static Code Analysis — Retail Point of Sale & Discount Tracker

## 1. Overview

This project focuses on improving the code quality, security, style, and maintainability of a Python-based Retail Point of Sale (POS) system using three static analysis tools: **Pylint, Bandit, and Flake8**.

The assigned source file is `pos_system.py`.

The program simulates checkout operations for a small shop, calculates totals with tax, applies promotional codes, maintains a running sales total, and appends receipt information to `pos_log.txt`.

Although the original program runs, it contains several code-quality, security, formatting, and input-validation issues that can be identified and corrected using static analysis.

## 2. Objectives

- Understand the purpose of static code analysis.
- Identify common Python programming errors and security vulnerabilities.
- Use Pylint to evaluate code quality and maintainability.
- Use Bandit to detect potentially insecure coding patterns.
- Use Flake8 to identify style and formatting violations.
- Fix at least four identified issues and verify the changes.
- Improve the final Pylint score to above 9.5/10.
- Document the findings and reflect on the importance of static analysis.

## 3. About the Program

The Retail POS program provides the following functionality:

- Processes shopping carts and calculates subtotals.
- Applies tax rates to checkout totals.
- Supports promotional codes such as `total * 0.9` and `total - 50`.
- Maintains a running sales total.
- Generates receipt identifiers and records receipt information.
- Appends receipt details to `pos_log.txt`.

The program should validate checkout inputs and promo codes to avoid invalid calculations and unsafe execution.

## 4. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python 3 | Programming language |
| Pylint | Detects code-quality issues, naming problems, and potential programming errors |
| Bandit | Detects potentially insecure Python coding patterns |
| Flake8 | Checks Python style, whitespace, and formatting |
| Git | Tracks source-code changes and commits |
| Visual Studio Code | Code editing and terminal-based execution |

## 5. Environment Setup

### Step 1: Open the project

Open the project folder in Visual Studio Code and open its integrated terminal.

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install the analysis tools

```bash
python -m pip install pylint bandit flake8
```

Verify the installations:

```bash
pylint --version
bandit --version
flake8 --version
```

## 6. Run the Original Program

Before making changes, run:

```bash
python pos_system.py
```

Observe the checkout totals, promotional discounts, input handling, and sales summary. Try different promo-code inputs and check whether any output appears incorrect.

Save the initial analysis results before editing the source code.

## 7. Static Code Analysis

Run each tool against the original program and save its report.

### Pylint

```bash
pylint pos_system.py > pylint_report.txt
```

Pylint checks naming conventions, documentation, unused imports, exception handling, and other code-quality concerns.

### Bandit

```bash
bandit -r pos_system.py > bandit_report.txt
```

Bandit identifies potentially insecure coding patterns, including unsafe expression evaluation and problematic exception handling.

### Flake8

```bash
flake8 pos_system.py > flake8_report.txt
```

Flake8 identifies formatting violations, unused imports, whitespace problems, and other style issues.

The initial reports should be preserved so the original findings can be compared with the final results.

## 8. Issues Identified and Fixes Applied

The original program contained several issues, including:

| Issue | Tool | Fix approach |
|---|---|---|
| Unsafe use of `eval()` | Bandit, Pylint | Replaced arbitrary expression evaluation with validated promo-code parsing |
| Weak random-number generation | Bandit | Used `secrets.randbelow()` for receipt identifiers |
| Silent exception handling | Bandit, Pylint | Removed broad exception handling and silent error suppression |
| Mutable default argument | Pylint | Replaced the list default with `None` and initialized the list inside the function |
| Missing docstrings | Pylint | Added module and function documentation |
| Unused imports and variables | Pylint, Flake8 | Removed unnecessary code |
| File resource handling | Pylint | Used a context manager and explicit UTF-8 encoding |
| Naming convention violations | Pylint | Renamed functions to follow snake_case |
| Whitespace and blank-line violations | Flake8 | Corrected formatting and removed whitespace from blank lines |
| Invalid checkout inputs | Manual testing | Added validation for quantities and tax rates |

The complete issue table, including the original line numbers, descriptions, and detailed fixes, is maintained in `issues.md`.

## 9. Code Improvements

The updated implementation includes:

- Safer promo-code parsing without `eval()`.
- Improved exception handling and input validation.
- Safe initialization of default list arguments.
- Improved receipt identifier generation.
- Explicit file encoding and resource management.
- Consistent function naming and documentation.
- Corrected formatting and whitespace.
- Validation to prevent negative quantities and invalid tax rates.

## 10. Verification After Fixes

After updating `pos_system.py`, rerun all three analysis tools.

```bash
pylint pos_system.py
bandit -r pos_system.py
flake8 pos_system.py
```

Run the program again:

```bash
python pos_system.py
```

Verify that the program completes successfully, checkout totals are valid, and supported promotional codes work correctly.

### Final verification results

- **Pylint:** 10.00/10.
- **Bandit:** No issues identified.
- **Flake8:** No reported violations.
- **Program execution:** Completed successfully with valid demonstration checkout inputs.

The results above reflect the final checks performed during this lab.

## 11. Git Version Control

Git is used to track the changes made during the lab.

Check the current status:

```bash
git status
```

Review recent commits:

```bash
git log --oneline
```

The lab handout requires three commits corresponding to fixes associated with the three analysis tools. Each commit should contain genuine, relevant changes and have a descriptive message.

## 12. Deliverables

The following items are required for submission:

1. **`pos_system.py`** — the cleaned and updated Python source file, with at least four issues fixed.
2. **`issues.md`** — the completed issue table containing issue names, types, original line numbers, descriptions, and fix approaches.
3. **`reflection.md`** — answers to the four reflection questions specified in the lab handout.
4. **Analysis reports** — Pylint, Bandit, and Flake8 reports from before and after the fixes, as required by the handout.
5. **Three Git commits** — meaningful commits documenting the changes made during the lab.

## 13. Conclusion

This lab demonstrates how static code analysis can improve Python software quality, security, and maintainability. Pylint helped identify code-quality problems, Bandit highlighted potentially unsafe coding patterns, and Flake8 detected formatting violations.

By correcting the reported issues and rerunning the analysis tools, the Retail POS program achieved a Pylint score of 10.00/10, no reported Bandit findings, and no Flake8 violations.

The exercise also demonstrates that successful program execution alone does not guarantee secure, maintainable, or correctly validated software.
