
from hypothesis import given, strategies as st
from processor import sanitize_license_plate, parse_trip_mileage, format_rental_invoice


@given(st.text() | st.none())
def test_sanitize_license_plate_no_crash(s):
    try:
        sanitize_license_plate(s)
    except (TypeError, ValueError):
        pass
    except Exception as e:
        assert False, f"Unexpected crash in sanitize_license_plate: {e}"


@given(st.text() | st.none())
def test_parse_trip_mileage_safe(s):
    try:
        parse_trip_mileage(s)
    except (TypeError, ValueError):
        pass
    except Exception as e:
        assert False, f"Unexpected crash in parse_trip_mileage: {e}"


@given(st.text() | st.none())
def test_format_rental_invoice_safe(s):
    try:
        format_rental_invoice(s)
    except (TypeError, ValueError):
        pass
    except Exception as e:
        assert False, f"Unexpected crash in format_rental_invoice: {e}"
