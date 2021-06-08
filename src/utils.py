def get_risk(bmi):
    if bmi < 18.5:
        return "Malnutrition"
    if bmi < 24.9:
        return "Low"
    if bmi < 29.9:
        return "Enhanced"
    if bmi < 34.9:
        return "Medium"
    if bmi < 39.9:
        return "High"
    else:
        return "Very High"


def get_bmi(weight, height):
    try:
        return weight/((height/100)**2)
    except ZeroDivisionError as e:
        print("Zero Devision error", e)
        # negative result shows zero division error
        return -1
