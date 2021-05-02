import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from skimage import color
from skimage import io


def display():
    # Place for filename
    filename = 'ptaszek.png'
    # Read image date
    png = Image.open(filename)
    # Display image
    png.show()
    print(png.format)


# Problems not with fft but with the cool way to display of data

filename = 'ptaszek.png'
# Open image
png = io.imread(filename)
# Image is converted to greyscale with formula L = R * 299/1000 + G * 587/1000 + B * 114/1000
png_gray = color.rgb2gray(png)
# We make a 2D discrete fft of image
fft_png = np.fft.fft2(png)
# Now we make a shift of fourier as on CPOIS
pretty_fft = np.fft.fftshift(fft_png)

plt.figure(1)
plt.subplot(131), plt.imshow(png_gray, cmap='gray')
plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(png_gray)
plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(png_gray)
plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.show()
