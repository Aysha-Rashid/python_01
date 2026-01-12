import numpy as np


def give_bmi(height: float | int, weight: float | int):
    """Takes height and weight and returns BMI"""
    try:
        height = np.array(height, dtype=float)
        weight = np.array(weight, dtype=float)
        if height.shape != weight.shape:
            raise ValueError("height and weight must have the same length")
        return (weight / (height ** 2)).tolist()
    except Exception as e:
        print("Error occured: ", e)
        return []


def apply_limit(bmi: list, limit: int):
    try:
        bmi = np.array(bmi, dtype=float)
    except Exception as e:
        print("Error occured:", e)
        return []
    return (bmi > limit).tolist()
