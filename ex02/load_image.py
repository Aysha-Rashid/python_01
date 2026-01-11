import array as array
import matplotlib.pyplot as plt


def ft_load(path: str) -> array:
    """Loads the image using mpimg.iread and returns img."""
    try:
        img = plt.imread(path)
        print("The shape of image is:", img.shape)
    except Exception as e:
        print("Error: cannot load image")
        return []
    return (img)

print(ft_load("someStuff.txt"))
