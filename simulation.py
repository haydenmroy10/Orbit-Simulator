# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

G = 6.67430e-11  # Gravitational constant

mass_earth = 5.972e24  #Mass of Earth in kg
mass_moon = 7.342e22  #Mass of Moon in kg

GRAV_CONSTANT = G * mass_earth * mass_moon

sim_duration = float(input("Enter simulation duration in Years: "))
# Initial conditions
earth_position = [0.0, 0.0]  #List containing x and y coordinates of the Earth
earth_velocity = [0.0, 0.0]  # Initial velocity of Earth (m/s)
moon_position = [384.4e6, 0.0]  # Initial position of Moon (m)
moon_velocity = [0.0, 1022.0]  #Initial X and Y velocities of the moon in (m/s)

# Time parameters
dt = 1000.0  # Time step in seconds
t = 0  #Time elapsed in simulation

#Lists that store the positions of the Earth and Moon at each timestep
earth_coordinates = []
moon_coordinates = []

def Euler():
    t = 0 #Time elapsed in simulation
    dt = 1000 #Time between time steps in seconds
    while t < sim_duration * 31536000:
        
        # Calculate the distance between Earth and Moon
        rx = moon_position[0] - earth_position[0]
        ry = moon_position[1] - earth_position[1]
        r = (rx**2 + ry**2)**0.5
        
        # Calculate gravitational forces
        force_on_earth = [GRAV_CONSTANT / r**2 * rx / r, GRAV_CONSTANT / r**2 * ry / r]
        force_on_moon = [-GRAV_CONSTANT / r**2 * rx / r, -GRAV_CONSTANT / r**2 * ry / r]
        
        
        earth_position[0] += earth_velocity[0] * dt
        earth_position[1] += earth_velocity[1] * dt
        earth_velocity[0] += force_on_earth[0] / mass_earth * dt
        earth_velocity[1] += force_on_earth[1] / mass_earth * dt
        
        #Updates moon position based on the instantaneus velocity
        moon_position[0] += moon_velocity[0] * dt
        moon_position[1] += moon_velocity[1] * dt
        
        #Updates moon velocity based on gravitational force on the moon
        moon_velocity[0] += force_on_moon[0] / mass_moon * dt
        moon_velocity[1] += force_on_moon[1] / mass_moon * dt
        
        # Adds coordinates to list of coordinates
        earth_coordinates.append(earth_position.copy())
        moon_coordinates.append(moon_position.copy())
        
        #increments time
        t += dt
        
Euler()

#Plot creation
plt.figure(figsize=(8, 8))
plt.plot([pos[0] for pos in earth_coordinates], [pos[1] for pos in earth_coordinates], label='Earth')
plt.plot([pos[0] for pos in moon_coordinates], [pos[1] for pos in moon_coordinates], label='Moon')
plt.title('Earth and Moon Orbit Simulation using Euler\'s Method')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.legend()
plt.show()