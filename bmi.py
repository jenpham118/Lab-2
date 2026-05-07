def calculate_bmi(height, weight):
    bmi = weight / (height**2)

    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Under weight")
        return -1
    elif bmi < 25:
        print("Normal")
        return 0
    else:
        print("Overweight")
        return 1

calculate_bmi(height=1.73, weight=57)