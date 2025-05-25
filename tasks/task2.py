import matplotlib.pyplot as plt
import numpy as np
plt.style.use("dark_background")

def task2(planets, dimensions = "2D"):
    theta = np.linspace(0, 2 * np.pi, 1000)
    fig = plt.figure(figsize=(12, 10))

    if dimensions == "3D":
        ax = fig.add_subplot(111, projection="3d")
        ax.view_init(elev = 26, azim = -133)
    
    for planet in planets:
        r = planet.semi_major_axis * (1 - planet.orbital_eccentricity ** 2) / (1 - planet.orbital_eccentricity * np.cos(theta))
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        if dimensions == "3D":
            beta = planet.orbital_inclination * np.pi / 180
            xx = x * np.cos(beta)
            zz = x * np.sin(beta)
            yy = y
            color = tuple(c / 255 for c in planet.color)
            ax.plot(xx, yy, zz, color = color, linestyle = "-", linewidth = 3, label = planet.name)
        
        else:
            color = tuple(c / 255 for c in planet.color)
            plt.plot(x, y, color = color, label = planet.name)
        
        if dimensions == "3D":
            ax.set_xlabel("X / AU")
            ax.set_ylabel("Y / AU")
            ax.set_zlabel("Z / AU")
            ax.set_title("Orbital Paths of Planets")
            ax.legend()
        
        else:
            plt.xlabel("X / AU")
            plt.ylabel("Y / AU")
            plt.title("Orbital Paths of Planets")
            plt.legend()
        
    return fig