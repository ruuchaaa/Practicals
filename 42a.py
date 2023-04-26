import matplotlib.pyplot as plt

# Create some example data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a histogram
plt.hist(data)

# Set the title and axis labels
plt.title('Histogram of Example Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Display the plot
plt.show()
