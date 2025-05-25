import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def task3(planets, limits):
    fig, ax = plt.subplots()
    ax.set_xlim(-limits, limits)
    ax.set_ylim(-limits, limits)
    
    lines = []
    markers = []

    for planet in planets:
        line, = ax.plot([], [], lw=1)
        
        color = tuple(c / 255 for c in planet.color)
        marker, = ax.plot([], [], marker= "*", markersize=8, color = color , label = planet.name)
        lines.append(line)
        markers.append(marker)

    sun, = ax.plot([], [], marker= "o", color= "yellow", markersize= 20, label = "Sun")  # Increase the sun marker size
    
    def init():
        for line in lines:
            line.set_data([], [])
        for marker in markers:
            marker.set_data([], [])
        sun.set_data([], [])
        return lines + markers + [sun]
    
    def animate(frame):
        for i, planet in enumerate(planets):
            planet.true_anomaly += planet.mean_motion * 0.02  # Adjust animation speed
            eccentric_anomaly = planet.true_anomaly
            radius = planet.semi_major_axis * (1 - planet.orbital_eccentricity ** 2) / (1 + planet.orbital_eccentricity * np.cos(planet.true_anomaly))
            x = radius * np.cos(planet.true_anomaly)
            y = radius * np.sin(planet.true_anomaly)
            lines[i].set_data(x, y)
            markers[i].set_data(x, y)
            
        sun.set_data(0, 0)
        return lines + markers + [sun]


    anim = FuncAnimation(fig, animate, init_func=init, frames=1000, interval=50, blit=True)
    ax.legend()

    plt.show()