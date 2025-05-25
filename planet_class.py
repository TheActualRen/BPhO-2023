import numpy as np
import math
import pygame 


class Planet:
    AU = 148.6e6 * 1000
    G = 6.67428e-11
    TIMESTEP = 3600 * 125
    
    def __init__(self, 
                 name, 
                 mass, 
                 semi_major_axis, 
                 orbital_eccentricity, 
                 orbital_inclination, 
                 initial_polar_angle, 
                 radius, 
                 rotational_period, 
                 orbital_period, 
                 color,
                 y_vel):
        
        self.name = name
        self.mass = mass
        self.semi_major_axis = semi_major_axis
        self.orbital_eccentricity = orbital_eccentricity
        self.orbital_inclination = orbital_inclination
        self.initial_polar_angle = initial_polar_angle
        self.radius = radius
        self.rotational_period = rotational_period
        self.orbital_period = orbital_period
        self.color = color

        self.mean_motion = 2 * np.pi / self.orbital_period
        self.true_anomaly = 0 

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        
        self.x = self.semi_major_axis * self.AU
        self.y = 0

        self.x_vel = 0
        self.y_vel = y_vel



    def draw(self, win, WIDTH, HEIGHT, SCALE):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)


    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets, TIMESTEP):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * TIMESTEP
        self.y_vel += total_fy / self.mass * TIMESTEP

        self.x += self.x_vel * TIMESTEP
        self.y += self.y_vel * TIMESTEP
        self.orbit.append((self.x, self.y))

  
  
