import matplotlib.pyplot as plt
import numpy as np

def particle_motion(initial_position, initial_velocity, acceleration, time):
    positions = []
    velocities = []
    for t in range(time):
        position = initial_position + initial_velocity * t + 0.5 * acceleration * t**2
        velocity = initial_velocity + acceleration * t
        positions.append(position)
        velocities.append(velocity)
    return positions, velocities

# Inputs data
initial_pos = 0
initial_vel = 5
acceleration = 2
total_time = 10

positions, velocities = particle_motion(initial_pos, initial_vel, acceleration, total_time)

# Plotting
time = np.arange(total_time)
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(time, positions, marker='o')
plt.title('Particle Position over Time')
plt.xlabel('Time')
plt.ylabel('Position')

plt.subplot(2, 1, 2)
plt.plot(time, velocities, marker='o')
plt.title('Particle Velocity over Time')
plt.xlabel('Time')
plt.ylabel('Velocity of particle')

plt.tight_layout()
plt.show()
