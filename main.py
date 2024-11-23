import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = np.zeros((height, width))
    for row in range(height):
        for col in range(width):
            x = x_min + (x_max - x_min) * col / width
            y = y_min + (y_max - y_min) * row / height
            c = complex(x, y)
            image[row, col] = mandelbrot(c, max_iter)
    return image

def plot_mandelbrot(image, x_min, x_max, y_min, y_max):
    plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap="hot", origin="lower")
    plt.colorbar(label="Iterations")
    plt.title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

if __name__ == "__main__":
    print("Starting Mandelbrot visualization...")
    width, height = 500, 500
    x_min, x_max, y_min, y_max = -2.5, 1.0, -1.5, 1.5
    max_iter = 100

    print("Generating Mandelbrot set...")
    mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
    print("Plotting Mandelbrot set...")
    plot_mandelbrot(mandelbrot_image, x_min, x_max, y_min, y_max)
