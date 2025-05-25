import matplotlib.pyplot as plt

def task1(planets):
    fig = plt.figure(figsize=(12, 10))
    orbital_period_squared = []
    semi_major_axis_cubed = []

    for planet in planets:
        orbital_period_squared.append(planet.orbital_period ** 2) 
        semi_major_axis_cubed.append(planet.semi_major_axis ** 3)
    
    plt.plot(semi_major_axis_cubed, orbital_period_squared)
    plt.xlabel("Semi Major Axis Cubed / AU", fontsize=12)
    plt.ylabel("Orbital Period Squared / AU", fontsize=12)

    return fig
    