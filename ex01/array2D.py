import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        a = np.array(family, dtype=float)
        if not isinstance(family, list):
            raise TypeError("invalid type")
        print("My shape is :", a.shape)
        sliceStore = a[start: end]
        print("My new shape is :", sliceStore.shape)
    except Exception as e:
        print("Error :", e)
        return []
    return (sliceStore.tolist())

family = [[1.80, 78.4],
[2.15],
[2.10, 98],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))