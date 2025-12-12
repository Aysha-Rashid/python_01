import numpy as np

def give_bmi(height, weight):
    try: 
        height = np.array(height, dtype=float)
        weight = np.array(weight, dtype=float)
        print("height checking : ", height)
        print("weight checking : ", weight)

        if height.shape != weight.shape:
            raise ValueError("height and weight must have the same length")
        return (weight / (height ** 2)).tolist()
    except Exception as e:
        print("Error occured: ", e)
        return []

def apply_limit(bmi, limit: int):
    bmi = np.array(bmi, dtype=float)
    return (bmi > limit).tolist()


# Example
h = [1.70, 1.82, 3]
w = [65, 85, 45]

bmi_values = give_bmi(h, w)
print(bmi_values)

print(apply_limit(bmi_values, 25))


# BmiList = give_bmi([2.71, 1.15], [165.3, 38.4])
# print("BMI:", BmiList)
# print("Checking:", apply_limit(BmiList, 26))


# probably wrong because i was supposed to use numpy.array for this
