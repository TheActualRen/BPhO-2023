import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def task4(planets):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")

    sun_marker = ax.scatter([0], [0], [0], color = "yellow", s = 300, marker = "o", label = "Sun")

    for planet in planets:
        theta = np.linspace(0, 2 * np.pi , 1000)
        r = planet.semi_major_axis * (1 - planet.orbital_eccentricity ** 2) / (1 - planet.orbital_eccentricity * np.cos(theta))    
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        beta = planet.orbital_inclination * np.pi / 180
        zz = y * np.tan(beta)

        color = tuple(c / 255 for c in planet.color)
        ax.plot(x, y, zz, linewidth = 1.5, color = color, label = planet.name)
    
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Planetary Orbits")
    ax.legend()

    def animate(frame):
        ax.clear()

        max_distance = max(planet.semi_major_axis for planet in planets)
        ax.set_xlim(-max_distance, max_distance)
        ax.set_ylim(-max_distance, max_distance)
        ax.set_zlim(-max_distance, max_distance)

        for planet in planets:
            planet.true_anomaly += planet.mean_motion * 0.02
            
            if planet.name in ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]:
                timestep = 1 if planet.name == "Jupiter" else planet.orbital_period / 1000
                planet.true_anomaly += planet.mean_motion * timestep
            
            eccentric_anomaly = planet.true_anomaly

            radius = planet.semi_major_axis * (1 - planet.orbital_eccentricity ** 2) / (1 + planet.orbital_eccentricity * np.cos(planet.true_anomaly))
            x = radius * np.cos(planet.true_anomaly)
            y = radius * np.sin(planet.true_anomaly)

            if planet.name == "Pluto":
                z = y * np.tan(planet.orbital_inclination * np.pi / 180)
            
            else:
                z = 0 
            
            ax.plot([x], [y], [z], marker = "o", markersize = 8, label = planet.name)

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("3D Planetary Orbits")
        ax.legend()

        ax.scatter([0], [0], [0], color = "yellow", s = 200, marker = "o")
    
    anim = FuncAnimation(fig, animate, frames = 1000, interval = 50)
    plt.show()