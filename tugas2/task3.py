"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 3:
Write a class that calculates and stores the height and weight of a person in metric. The BMI is calculated using this formula:
Weight/Height ^ 2 - weight is in kilograms and height is in meters.
The class should have two properties named:
Weight
Height
The class should have one method that returns a decimal named (no arguments should be accepted): BMI_Value.
"""

class PersonMetrics:
    def __init__(self, weight_kg, height_m):
        self.weight = weight_kg
        self.height = height_m

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

# Taking input and displaying output
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

person = PersonMetrics(weight, height)
print(f"BMI Value: {person.BMI_Value():.2f}")

