def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity"


def main():
    print("BMI Calculator")
    print("Learning project - not medical advice")

    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
