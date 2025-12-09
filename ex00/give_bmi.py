import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    # so we divide the weight with the square of height

    returnList = []
    j = 0
    for i,j  in zip(height, weight):
        result = j / i ** 2
        returnList.append(result)
 # using the keyword zip, i was able to go through two list parallel
    return returnList

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    checking = []
    for i in bmi:
        if i > limit:
            checking.append(True)
        else:
            checking.append(False)
    return (checking)


# BmiList = give_bmi([2.71, 1.15], [165.3, 38.4])
# print("BMI:", BmiList)
# print("Checking:", apply_limit(BmiList, 26))


# probably wrong because i was supposed to use numpy.array for this
