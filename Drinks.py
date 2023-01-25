import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_drink():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    drink = f.generate()
    # Add noise to the fractal shape to make it look more like a drink
    noise = np.random.normal(0, 0.05, drink.shape)
    drink = drink + noise
    drink = np.clip(drink, 0, 1)
    # Apply a drink-like color map to the fractal shape
    drink = plt.cm.YlOrBr(drink)
    # Return the fractal drink
    return drink

# Generate 10 fractal drink images
for i in range(10):
    drink = generate_fractal_drink()
    plt.imsave("fractal_drink_{}.png".format(i), drink)
