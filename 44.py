import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)

# Plot the data in each subplot
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sin(x)')
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cos(x)')
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Tan(x)')
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Exp(x)')

# Add a title for the entire figure
#fig.suptitle('Four Subplots')

# Display the plot
plt.show()
