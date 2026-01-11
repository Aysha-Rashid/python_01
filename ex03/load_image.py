from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load_image(path: str):
    try:
        testImg = plt.imread(path)
        print("The shape of image is:", testImg.shape)
        print(testImg)

        gray = np.mean(testImg, axis=2).astype(np.uint8)
        img1_resized = gray[:400, :400]
        img1_resized = img1_resized[:, :, np.newaxis]
        print("New shape after slicing:", img1_resized.shape)
        print(img1_resized)
        plt.title("Resize Image")
        plt.imshow(img1_resized, cmap="gray")
        plt.show()

    except Exception as e:
        print("Error:", e)
        return []

    return testImg

def main():
    img = load_image("animal.jpeg")
    # print(img)
    # plt.imshow(img)
    # zoom(img)

if __name__ == "__main__":
    main()