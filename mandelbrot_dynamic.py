import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mandelbrot(c, max_iter):
    """
    Calculate the number of iterations for the Mandelbrot set.

    Parameters:
        c (complex): The complex number being evaluated.
        max_iter (int): Maximum iterations to determine if a point diverges.

    Returns:
        int: Number of iterations before divergence, capped at max_iter.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Generate a Mandelbrot set image.

    Parameters:
        width (int): Width of the output image.
        height (int): Height of the output image.
        x_min (float): Minimum x-coordinate (real part).
        x_max (float): Maximum x-coordinate (real part).
        y_min (float): Minimum y-coordinate (imaginary part).
        y_max (float): Maximum y-coordinate (imaginary part).
        max_iter (int): Maximum iterations to determine divergence.

    Returns:
        numpy.ndarray: 2D array representing the Mandelbrot set.
    """
    image = np.zeros((height, width))
    for row in range(height):
        for col in range(width):
            x = x_min + (x_max - x_min) * col / width
            y = y_min + (y_max - y_min) * row / height
            c = complex(x, y)
            image[row, col] = mandelbrot(c, max_iter)
    return image

def update(frame, img, width, height, x_min, x_max, y_min, y_max):
    """
    Update function for the animation.

    Parameters:
        frame (int): The current frame of the animation.
        img (AxesImage): The image being updated.
    """
    max_iter = 50 + frame * 10  # Increase the maximum iterations over time
    x_mid, y_mid = -0.5, 0  # Center of the Mandelbrot set
    zoom = 1.5 - frame * 0.02  # Gradually zoom in

    new_x_min = x_mid - zoom
    new_x_max = x_mid + zoom
    new_y_min = y_mid - zoom
    new_y_max = y_mid + zoom

    # Generate the new Mandelbrot set
    mandelbrot_image = mandelbrot_set(
        width, height, new_x_min, new_x_max, new_y_min, new_y_max, max_iter
    )

    # Update the image data
    img.set_data(mandelbrot_image)
    img.set_extent((new_x_min, new_x_max, new_y_min, new_y_max))
    return img,

if __name__ == "__main__":
    # Parameters
    width, height = 500, 500
    x_min, x_max = -2.5, 1.0
    y_min, y_max = -1.5, 1.5

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title("Dynamic Mandelbrot Set")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    
    # Initial Mandelbrot image
    initial_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, 50)
    img = ax.imshow(initial_image, extent=(x_min, x_max, y_min, y_max), cmap="hot", origin="lower")

    # Animate the Mandelbrot set
    anim = FuncAnimation(
        fig,
        update,
        frames=100,  # Number of frames
        interval=100,  # Time in ms between frames
        fargs=(img, width, height, x_min, x_max, y_min, y_max),
        blit=True,
    )

    # Display the animation
    plt.show()
