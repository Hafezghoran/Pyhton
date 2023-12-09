import matplotlib.pyplot as plt

# Positions and corresponding times
positions = [0, 2, 4, 6, 8]  # List of positions
times = [0, 1, 2, 3, 4]  # Corresponding list of times

# Plotting the position over time
plt.plot(times, positions, marker='o', linestyle='-')  # Plotting positions against times
plt.title('Particle Position over Time')  # Title of the plot
plt.xlabel('Time')  # Label for the x-axis
plt.ylabel('Position')  # Label for the y-axis
plt.grid(True)  # Display grid
plt.show()  # Display the plot
