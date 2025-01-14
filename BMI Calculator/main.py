def calculate_bmi(height, weight):
    """Calculate BMI using metric units."""
    bmi = weight / (height ** 2)
    return bmi


def get_bmi_category(bmi, age=None, gender=None):
    """Determine BMI category with optional age and gender considerations."""
    if age is not None and gender is not None:
        if gender.lower() == "male":
            if age < 18:
                return "Child/Teen BMI (consult a doctor for specifics)"
            elif bmi < 18.5:
                return "Underweight (Male)"
            elif bmi < 25:
                return "Normal weight (Male)"
            elif bmi < 30:
                return "Overweight (Male)"
            else:
                return "Obese (Male)"
        elif gender.lower() == "female":
            if age < 18:
                return "Child/Teen BMI (consult a doctor for specifics)"
            elif bmi < 18.5:
                return "Underweight (Female)"
            elif bmi < 24:
                return "Normal weight (Female)"
            elif bmi < 30:
                return "Overweight (Female)"
            else:
                return "Obese (Female)"
        else:
            return "Unknown gender. Using general BMI categories."

    if bmi < 16:
        return "Severely Underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese"
    else:
        return "Morbid obesity"


try:
    while True:
        print("\n" + "=" * 40)
        print("Welcome to BMI Calculator 1.0! Created by Aatif Muneeb Khan")
        print("=" * 40)

        try:
            height = float(input("Enter your height in meters: "))
            weight = float(input("Enter your weight in kilograms: "))
            age_input = input("Enter your age (optional, press Enter to skip): ")
            gender_input = input("Enter your gender (male/female, optional, press Enter to skip): ")

            # optional inputs for age and gender
            age = int(age_input) if age_input.strip() else None
            gender = gender_input.strip() if gender_input.strip() else None
        except ValueError:
            print("Invalid input. Please enter numeric values for height, weight, and age.")
            continue

        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi, age, gender)

        print("\n" + "-" * 40)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
        print("-" * 40)

        repeat = input("\nWould you like to calculate again? (yes to continue, any other key to exit): ").lower()
        if repeat != "yes":
            print("\nThank you for using the BMI Calculator. Goodbye!")
            break

except KeyboardInterrupt:
    print("\n\nProgram interrupted. Exiting the program. Goodbye!")
