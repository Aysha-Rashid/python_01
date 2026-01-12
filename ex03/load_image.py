import matplotlib.pyplot as plt


def load_image(path: str):
    """Loads the image using mpimg.iread, prints the
shape of the image and returns img."""
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise TypeError("Error: unsupported file format")
        img = plt.imread(path)
        print("The shape of image is:", img.shape)
        print(img)
        return (img)
    except Exception as e:
        print("Error:", e)
        return []
