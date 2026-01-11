import matplotlib.pyplot as plt
import numpy as np
# from rotate import rotate


def load_image(path: str):
    """Loads the image using mpimg.iread, cuts a square
from it and prints the shape of the image and returns img."""
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise TypeError("Error: unsupported file format")
        img = plt.imread(path)
        gray = np.mean(img, axis=2).astype(np.uint8)
        new_img = gray[100:500, 450:850, np.newaxis]
        plt.imshow(new_img, cmap="gray")
        plt.show()
        print("The shape of image is:", new_img.shape)
        print(new_img)
        return (img)
    except Exception as e:
        print("Error:", e)
        return []


def main():
    img = load_image("animal.jpeg")
    # rotate(img)


if __name__ == "__main__":
    main()
