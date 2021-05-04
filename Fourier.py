import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def display():
    # Place for filename
    filename = 'Images/ptaszek.png'
    # Read image date
    png = Image.open(filename)
    # Display image
    png.show()
    print(png.format)


def rgb2gray(png):
    return np.dot(png[..., :3], [0.2989, 0.5870, 0.1140])


def fourier(filename):

    # Open image
    png = Image.open(filename).convert('L')
    # We make a 2D discrete fft of image
    fft_png = np.fft.fft2(png)
    # Now we make a shift of fourier as on CPOIS
    pretty_fft = np.fft.fftshift(fft_png)

    magnitude = np.asarray(20*np.log10(np.abs(pretty_fft)), dtype=np.uint8)
    phase = np.asarray(np.angle(pretty_fft), dtype=np.uint8)

    plt.figure(1)
    plt.subplot(131), plt.imshow(png, cmap='gray')
    plt.title('Input'), plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(magnitude, cmap='gray')
    plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(phase, cmap='gray')
    plt.title('Phase'), plt.xticks([]), plt.yticks([])
    plt.show()
