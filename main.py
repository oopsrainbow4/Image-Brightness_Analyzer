import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# "medkit_phighting.png", "small_pixel_art_star.jpg" and "ten_cents_coin.jpg"
img = Image.open("ten_cents_coin.jpg")
convert_img = img.convert("L")

img_array = np.array(convert_img)

average_array = img_array.mean()
maxium_value_array = np.max(img_array)
minimal_value_array = np.min(img_array)

img_1d_array = img_array.ravel()

plt.hist(img_1d_array, bins=256)

plt.xlabel("x-Axis: Brightness (0 - 255)")
plt.ylabel("y-Axis: Amount of same brightness")
plt.title("Image Brightness Analyzer")

plt.show()

print(f"Average brightness: {round(average_array, 2)}")
print(f"Brightest  value: {maxium_value_array}")
print(f"Darkest value: {minimal_value_array}")

# convert_img.show()

# print(img_array)
# print(img_array.shape)