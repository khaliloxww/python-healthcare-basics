import csv


def load_patient_vitals(file_path):
    patients = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients.append({
                "patient_id": row["patient_id"],
                "age": int(row["age"]),
                "heart_rate": int(row["heart_rate"]),
                "systolic_bp": int(row["systolic_bp"]),
                "temperature_c": float(row["temperature_c"]),
            })
    return patients


def average(values):
    return sum(values) / len(values)


def get_alerts(patient):
    alerts = []

    if patient["heart_rate"] > 100:
        alerts.append("High heart rate")
    if patient["systolic_bp"] >= 140:
        alerts.append("High systolic blood pressure")
    if patient["temperature_c"] >= 38.0:
        alerts.append("Fever")

    return alerts


def main():
    patients = load_patient_vitals("patient_vitals.csv")

    avg_heart_rate = average([patient["heart_rate"] for patient in patients])
    avg_systolic_bp = average([patient["systolic_bp"] for patient in patients])
    avg_temperature = average([patient["temperature_c"] for patient in patients])

    print("Patient Vitals Summary")
    print("Learning project - not medical advice")
    print(f"Number of patients: {len(patients)}")
    print(f"Average heart rate: {avg_heart_rate:.1f} bpm")
    print(f"Average systolic blood pressure: {avg_systolic_bp:.1f} mmHg")
    print(f"Average temperature: {avg_temperature:.1f} C")
    print()
    print("Alerts:")

    found_alert = False
    for patient in patients:
        alerts = get_alerts(patient)
        if alerts:
            found_alert = True
            print(f"{patient['patient_id']}: {', '.join(alerts)}")

    if not found_alert:
        print("No alerts found.")


if __name__ == "__main__":
    main()
