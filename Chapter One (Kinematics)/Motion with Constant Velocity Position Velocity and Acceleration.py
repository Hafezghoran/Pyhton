import matplotlib.pyplot as plt
import numpy as np

# Generating time with different intervals
time = np.linspace(0, 10, 100)  # From 0 to 10 seconds with equal intervals

# Constant velocity
velocity = np.ones_like(time) * 5  # Constant velocity of 5

# Position by accumulating velocity values
position = np.cumsum(velocity) * (time[1] - time[0])  # Calculating position as cumulative sum

# Zero acceleration (assuming constant velocity)
acceleration = np.zeros_like(time)

# Displaying the plots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

ax1.plot(time, position)
ax1.set_title('Position vs Time')
ax1.set_xlabel('Time')
ax1.set_ylabel('Position')

ax2.plot(time, velocity)
ax2.set_title('Velocity vs Time')
ax2.set_xlabel('Time')
ax2.set_ylabel('Velocity')

ax3.plot(time, acceleration)
ax3.set_title('Acceleration vs Time')
ax3.set_xlabel('Time')
ax3.set_ylabel('Acceleration')

plt.tight_layout()
plt.show()
