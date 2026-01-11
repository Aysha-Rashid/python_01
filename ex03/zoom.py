import numpy as np
import matplotlib.pyplot as plt


def zoom(img: str):
    """Takes the img, convert it into grey and
then slice it to 400, 400 and then displays the img"""
    gray = np.mean(img, axis=2).astype(np.uint8)
    img_sliced = gray[100:500, 450:850, np.newaxis]
    print("New shape after slicing:", img_sliced.shape)
    print(img_sliced)
    plt.title("Sliced Image")
    plt.imshow(img_sliced, cmap="gray")
    plt.show()
