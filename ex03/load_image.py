from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load_image(path: str):
    try:
        testImg = Image.open(path)
        print("the size of the img:", testImg.size)

        img_array = np.array(testImg)
        print("The shape of image is:", img_array.shape)

        # Display original
        plt.imshow(img_array)
        plt.title("Original Image")
        plt.axis("off")
        plt.show()

        # Rotate and show
        rotated = testImg.rotate(90, expand=True)
        plt.imshow(np.array(rotated))
        plt.title("Rotated Image")
        plt.axis("off")
        plt.show()

        # Save rotated image
        rotated.save("rotated_image.jpeg")

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