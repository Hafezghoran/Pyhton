import matplotlib.pyplot as plt

# Time and constant velocity for a particle
time = [t for t in range(10)]  # Time
velocity = [5 for _ in range(10)]  # Constant velocity of 5

# Particle's position at each moment, assuming initial position is zero
position = [0]
for i in range(1, len(time)):
    position.append(position[i - 1] + velocity[i] * (time[i] - time[i - 1]))

# Plots
plt.figure(figsize=(12, 4))

# Position-time graph and displaying
plt.subplot(1, 2, 1)
plt.plot(time, position, marker='o')
plt.title('Position vs Time')
plt.xlabel('Time')
plt.ylabel('Position')

# Velocity-time graph
plt.subplot(1, 2, 2)
plt.plot(time, velocity, marker='o')
plt.title('Velocity vs Time')
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.tight_layout()
plt.show()
