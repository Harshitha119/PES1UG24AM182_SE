# L6_L7_02 — Car Rental Rate

## Lab 7: Fuzz Testing with Hypothesis

## About

This project implements property-based fuzz testing using **Hypothesis** to test the car rental rate processing application.

The fuzz tests target three functions:

- **License Plate Formatting:** Sanitizes vehicle license plates by removing delimiters and converting characters to uppercase.
- **Trip Mileage Processing:** Parses comma-separated mileage values into a list of floating-point numbers.
- **Rental Record Parsing:** Parses rental records and calculates the total rental cost based on the vehicle category and rental duration.

Hypothesis generates random and edge-case inputs to identify parsing errors, unexpected exceptions, and input-handling issues.

## Repository Structure

```text
L6_L7_02_car_rental_rate/
│
├── Lab 6/
│
└── Lab 7/
    ├── processor.py
    ├── test_processor.py
    └── README.md
```

## Files

| File | Description |
|------|-------------|
| `processor.py` | Fixed application module containing license plate sanitization, mileage parsing, and rental invoice processing. |
| `test_processor.py` | Hypothesis-based fuzz tests for the three processing functions. |
| `README.md` | Project description, setup instructions, and execution guide. |

## Requirements

- Python 3.11 or compatible Python version
- pytest
- Hypothesis

## Installation

Install the required testing libraries:

```bash
python -m pip install pytest hypothesis
```

## Running the Application

Navigate to the Lab 7 folder:

```bash
cd "Lab 7"
```

Run the application:

```bash
python processor.py
```

The application accepts:

- License plate input
- Comma-separated trip mileage values
- Rental record in `Driver:Days:Category` format

## Running Fuzz Tests

Execute the Hypothesis fuzz tests using pytest:

```bash
python -m pytest test_processor.py -v
```

Hypothesis automatically generates multiple inputs, including invalid and edge-case values, to verify that the processing functions handle inputs safely.

## Test Results

The following fuzz tests were executed successfully:

| Test | Description | Result |
|------|-------------|--------|
| `test_sanitize_license_plate_no_crash` | Tests license plate sanitization with generated inputs. | PASSED |
| `test_parse_trip_mileage_safe` | Tests mileage parsing with generated inputs. | PASSED |
| `test_format_rental_invoice_safe` | Tests rental record parsing with generated inputs. | PASSED |

**Final Result: 3 passed**

## Deliverables

1. PDF report containing application execution screenshots and fuzz testing results.
2. Fixed application Python script (`processor.py`).
3. Updated Hypothesis fuzz testing code (`test_processor.py`).

## Conclusion

This lab demonstrates the use of property-based fuzz testing with Hypothesis to identify edge cases and improve input handling in a car rental rate processing application.

The updated application and fuzz tests successfully execute, with all three tests passing.
