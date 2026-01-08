import numpy as np
import array as array
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def ft_load(path: str) -> array:
    """Loads the image using mpimg.iread and returns img."""
    try:
        img = mpimg.imread(path)
        print("The shape of image is:", img.shape)
    except Exception as e:
        print("Error:", e)
        return []
    return (img)

print(ft_load("./landscape.jpg"))