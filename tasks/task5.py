import numpy as np
import matplotlib.pyplot as plt

def task5(pluto):
# Function to calculate polar angle (theta) from orbital time (t)
    def polar_angle_from_time(t, period, eccentricity):
        mean_anomaly = 2 * np.pi * t / period
        eccentric_anomaly = mean_anomaly
        for _ in range(10):  # Iterative solution for eccentric anomaly
            next_eccentric_anomaly = eccentric_anomaly + (mean_anomaly - eccentric_anomaly + eccentricity * np.sin(eccentric_anomaly)) / (1 - eccentricity * np.cos(eccentric_anomaly))
            eccentric_anomaly = next_eccentric_anomaly
        true_anomaly = 2 * np.arctan2(np.sqrt(1 + eccentricity) * np.sin(eccentric_anomaly / 2), np.sqrt(1 - eccentricity) * np.cos(eccentric_anomaly / 2))
        theta = 2 * np.pi - true_anomaly
        return theta

    # Time points for calculation
    time_points = np.linspace(0, pluto.orbital_period, 1000)

    # Calculate polar angles for Pluto's orbit
    polar_angles_pluto = [polar_angle_from_time(t, pluto.orbital_period, pluto.orbital_eccentricity) for t in time_points]

    # Circular orbit with the same period as Pluto's orbit
    semi_major_axis_circular = pluto.semi_major_axis
    eccentricity_circular = 0  # Circular orbit
    polar_angles_circular = [polar_angle_from_time(t, pluto.orbital_period, eccentricity_circular) for t in time_points]

    # Plotting
    fig = plt.figure(figsize=(10, 6))
    plt.plot(time_points, polar_angles_pluto, label='Pluto Orbit')
    plt.plot(time_points, polar_angles_circular, label='Circular Orbit')
    plt.xlabel('Orbital Time (years)')
    plt.ylabel('Polar Angle (radians)')
    plt.title('Variation of Polar Angle with Time')
    plt.legend()
    plt.grid()
    return fig