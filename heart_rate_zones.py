def estimate_max_heart_rate(age):
    return 220 - age


def calculate_zone(max_heart_rate, lower_percent, upper_percent):
    lower = max_heart_rate * lower_percent
    upper = max_heart_rate * upper_percent
    return round(lower), round(upper)


def main():
    print("Heart Rate Zones Calculator")
    print("Learning project - not medical advice")

    age = int(input("Enter age: "))
    max_heart_rate = estimate_max_heart_rate(age)

    zones = {
        "Light intensity": calculate_zone(max_heart_rate, 0.50, 0.60),
        "Moderate intensity": calculate_zone(max_heart_rate, 0.60, 0.70),
        "High intensity": calculate_zone(max_heart_rate, 0.70, 0.85),
    }

    print(f"Estimated maximum heart rate: {max_heart_rate} bpm")
    for zone_name, (lower, upper) in zones.items():
        print(f"{zone_name}: {lower}-{upper} bpm")


if __name__ == "__main__":
    main()
