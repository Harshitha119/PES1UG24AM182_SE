
import pytest
from car_rental_rate import process_rental_fleet, check_fleet_telematics


def test_standard_economy_rental():
    result = process_rental_fleet(
        [{"is_confirmed": True, "vehicle_type": "economy",
          "driver_age": 30, "days": 2, "trip_segments": [100]}], 10.0
    )
    assert result == {"total_revenue": 110.0, "status": "STANDARD"}


def test_luxury_young_driver():
    result = process_rental_fleet(
        [{"is_confirmed": True, "vehicle_type": "luxury",
          "driver_age": 20, "days": 2, "trip_segments": [301, 50]}], 10.0
    )
    assert result == {"total_revenue": 600.0, "status": "STANDARD"}


def test_suv_young_driver():
    result = process_rental_fleet(
        [{"is_confirmed": True, "vehicle_type": "suv",
          "driver_age": 24, "days": 1, "trip_segments": [50]}], 5.0
    )
    assert result == {"total_revenue": 105.0, "status": "STANDARD"}


def test_unconfirmed_rental():
    result = process_rental_fleet([{"is_confirmed": False}], 10.0)
    assert result["status"] == "EMPTY_BATCH"


def test_invalid_days():
    result = process_rental_fleet(
        [{"is_confirmed": True, "days": 0}], 10.0
    )
    assert result["status"] == "EMPTY_BATCH"


def test_negative_mileage():
    result = process_rental_fleet(
        [{"is_confirmed": True, "days": 1, "trip_segments": [-5]}], 0.0
    )
    assert result == {"total_revenue": 40.0, "status": "STANDARD"}


def test_high_risk_audit():
    result = process_rental_fleet(
        [{"is_confirmed": True, "days": 1,
          "trip_segments": [-1, -2, -3, -4, -5]}], 0.0
    )
    assert result == {
        "total_revenue": 40.0, "status": "HIGH_RISK_AUDIT"
    }


def test_invalid_rentals():
    with pytest.raises(ValueError):
        process_rental_fleet("invalid", 10.0)


def test_negative_admin_fee():
    with pytest.raises(ValueError):
        process_rental_fleet([], -1.0)


def test_empty_telematics():
    assert check_fleet_telematics([]) == "NO_DATA"
    assert check_fleet_telematics(None) == "NO_DATA"


def test_safe_telematics():
    assert check_fleet_telematics([[60, 105, 80, 70]]) == "SAFE"


def test_consecutive_speeding():
    assert check_fleet_telematics([[105, 110]]) == "GROUND_VEHICLE"
