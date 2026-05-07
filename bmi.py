def calculate_bmi(height, weight):
    bmi = weight / (height**2)

    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Under weight")
    elif bmi < 25:
        print("Normal")
    else:
        print("Overweight")

calculate_bmi(height=1.73, weight=57)