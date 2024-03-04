#input
 
# Asks the user to enter four values:
# gender
# birthdate in this format: YYYY-MM-DD
# weight in U.S. pounds
# height in U.S. inches
 
#processing
 
# Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
# Converts inches to centimeters (1 in = 2.54 cm).
# Calculates age, BMI, and BMR.
 
#output
# Prints age, weight in kg, height in cm, BMI, and BMR.
 
# Import datetime so that it can be
# used to compute a person's age.
 
from datetime import datetime
 
 
def main():
    # Get the user's gender, birthdate, height, and weight.
    # Please enter your gender (M or F):
    gender = input("Please enter your gender (M or F): ")
    # Enter your birthdate (YYYY-MM-DD):
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    # Enter your weight in U.S. pounds: 125
    pounds = float(input("Enter your weight in U.S. pounds: "))
    # Enter your height in U.S. inches:
    inches = float(input("Height in U.S. inches: "))
    
 
    years = compute_age(birthdate)
    weight_kg = kg_from_lb(pounds)
    hight_cm = cm_from_in(inches)
    bmi = body_mass_index(weight_kg, hight_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, hight_cm, years)  
    
 
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    # Body mass index:
    # Print the results for the user to see.
    
    print(f"Age (years): {years}")
    print(f"Weight (kg): {weight_kg:.2f}")
    print(f"Height (cm): {hight_cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")
    pass
 
 
def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
 
    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year
 
    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
 
    return years
 
 
def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    
    weight_kg = (pounds * 0.45359237)
    
    return weight_kg  
 
 
def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    hight_cm = (inches * 2.54)
    
    return hight_cm
 
def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / (height ** 2) * 10000
    return bmi
 
 
def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper == "F":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    #error condion
        return bmr
 
main()
 
# Call the main function so that
# this program will start executing.
