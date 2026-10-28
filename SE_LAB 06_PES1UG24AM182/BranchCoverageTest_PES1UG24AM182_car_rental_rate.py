
import pytest
from car_rental_rate import process_rental_fleet, check_fleet_telematics


def test_invalid_input_branches():
    with pytest.raises(ValueError):
        process_rental_fleet("invalid", 10)

    with pytest.raises(ValueError):
        process_rental_fleet([], -1)


def test_empty_and_unconfirmed_batches():
    assert process_rental_fleet([], 10) == {
        "total_revenue": 0.0,
        "status": "EMPTY_BATCH"
    }

    result = process_rental_fleet(
        [{"is_confirmed": False}], 10
    )
    assert result["status"] == "EMPTY_BATCH"


def test_default_values_and_economy_rate():
    result = process_rental_fleet(
        [{"is_confirmed": True}], 0
    )
    assert result == {
        "total_revenue": 40.0,
        "status": "STANDARD"
    }


def test_invalid_days_branch():
    result = process_rental_fleet(
        [{"is_confirmed": True, "days": 0}], 0
    )
    assert result["status"] == "EMPTY_BATCH"


def test_all_vehicle_types():
    rentals = [
        {"is_confirmed": True, "vehicle_type": "luxury",
         "driver_age": 30, "days": 1},
        {"is_confirmed": True, "vehicle_type": "suv",
         "driver_age": 30, "days": 1},
        {"is_confirmed": True, "vehicle_type": "economy",
         "driver_age": 30, "days": 1},
    ]

    result = process_rental_fleet(rentals, 0)
    assert result["total_revenue"] == 230.0
    assert result["status"] == "STANDARD"


def test_mileage_negative_boundary_and_long_trip():
    result = process_rental_fleet(
        [{"is_confirmed": True, "driver_age": 30, "days": 1,
          "trip_segments": [-1, 0, 300, 301]}], 0
    )

    assert result == {
        "total_revenue": 220.4,
        "status": "STANDARD"
    }


def test_long_trip_with_driver_under_21():
    result = process_rental_fleet(
        [{"is_confirmed": True, "driver_age": 20, "days": 1,
          "trip_segments": [301, 100]}], 0
    )

    assert result == {
        "total_revenue": 310.0,
        "status": "STANDARD"
    }


def test_long_trip_with_driver_age_21():
    result = process_rental_fleet(
        [{"is_confirmed": True, "driver_age": 21, "days": 1,
          "trip_segments": [301]}], 0
    )

    assert result["total_revenue"] == 180.4


def test_young_luxury_and_nonluxury_surcharges():
    rentals = [
        {"is_confirmed": True, "vehicle_type": "luxury",
         "driver_age": 24, "days": 2},
        {"is_confirmed": True, "vehicle_type": "economy",
         "driver_age": 24, "days": 2},
    ]

    result = process_rental_fleet(rentals, 0)
    assert result["total_revenue"] == 460.0


def test_high_risk_threshold():
    result = process_rental_fleet(
        [{"is_confirmed": True, "days": 1,
          "trip_segments": [-1, -2, -3, -4, -5]}], 0
    )

    assert result["status"] == "HIGH_RISK_AUDIT"


def test_telematics_empty_and_none():
    assert check_fleet_telematics([]) == "NO_DATA"
    assert check_fleet_telematics(None) == "NO_DATA"


def test_telematics_safe_and_streak_reset():
    assert check_fleet_telematics([[101, 80, 102]]) == "SAFE"


def test_telematics_two_consecutive_speeding_readings():
    assert check_fleet_telematics([[101, 102]]) == "GROUND_VEHICLE"


def test_telematics_streak_resets_between_vehicles():
    assert check_fleet_telematics([[101], [102]]) == "SAFE"
