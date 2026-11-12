
import math


def sanitize_license_plate(plate):
    if not isinstance(plate, str):
        raise TypeError("License plate must be a string")

    plate = plate.strip()

    for ch in ['-', ' ', '_', '#']:
        plate = plate.replace(ch, '')

    plate = plate.upper()

    if not plate:
        raise ValueError("License plate cannot be empty")

    if not plate.isalnum():
        raise ValueError("License plate contains invalid characters")

    return plate


def parse_trip_mileage(mileage_csv):
    if not isinstance(mileage_csv, str):
        raise TypeError("Mileage input must be a string")

    if not mileage_csv.strip():
        raise ValueError("Mileage input cannot be empty")

    parts = mileage_csv.split(',')
    mileages = []

    for m in parts:
        m = m.strip()

        if not m:
            raise ValueError("Mileage value cannot be empty")

        try:
            mileage = float(m)
        except ValueError:
            raise ValueError(f"Invalid mileage value: {m}")

        if not math.isfinite(mileage):
            raise ValueError("Mileage must be finite")

        if mileage < 0:
            raise ValueError("Mileage cannot be negative")

        mileages.append(mileage)

    return mileages


def format_rental_invoice(record):
    if not isinstance(record, str):
        raise TypeError("Rental record must be a string")

    parts = record.split(':')

    if len(parts) != 3:
        raise ValueError("Rental record must contain Driver:Days:Category")

    driver = parts[0].strip()

    if not driver:
        raise ValueError("Driver name cannot be empty")

    try:
        days = int(parts[1].strip())
    except ValueError:
        raise ValueError("Rental days must be an integer")

    if days <= 0:
        raise ValueError("Rental days must be positive")

    category = parts[2].strip()

    if not category:
        raise ValueError("Rental category cannot be empty")

    daily_rate = 50.0 if category.lower() == "suv" else 30.0

    total = days * daily_rate

    return (
        f"Driver {driver} booked {category} for {days} days: "
        f"Total ${total:.2f}"
    )


def main():
    print("==== Running sanitize_license_plate ====")
    raw_plate = input("Enter license plate with delimiters (-, _, #): ")

    try:
        clean_plate = sanitize_license_plate(raw_plate)
        print("Sanitized Plate:", clean_plate)
    except (TypeError, ValueError) as e:
        print("Invalid license plate:", e)

    print("\n==== Running parse_trip_mileage ====")
    csv_input = input("Enter CSV of mileages (e.g. 100.5, 45.2, 80.0): ")

    try:
        mileage_list = parse_trip_mileage(csv_input)
        print("Parsed Mileage List:", mileage_list)
    except (TypeError, ValueError) as e:
        print("Invalid mileage:", e)

    print("\n==== Running format_rental_invoice ====")
    record_input = input("Enter rental record (Driver:Days:Category): ")

    try:
        invoice = format_rental_invoice(record_input)
        print("Rental Invoice:", invoice)
    except (TypeError, ValueError) as e:
        print("Invalid rental record:", e)


if __name__ == "__main__":
    main()
