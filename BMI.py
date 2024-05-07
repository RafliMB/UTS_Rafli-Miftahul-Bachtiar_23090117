def bmi():
    if bmi < 18.5:
        print("Berat badan kurang")
        return bmi
    elif bmi >= 18.5 and bmi < 24.9:
        print("Berat badan normal")
        return bmi
    elif bmi >= 25 and bmi < 29.9:
        print("Kelebihan berat badan")
        return bmi
    elif bmi >= 30:
        print("Obesitas")
        return bmi