from tasks.task1 import * 
from tasks.task2 import *
from tasks.task3 import *
from tasks.task4 import *
from tasks.task5 import *
from tasks.task6 import *
from tasks.task7 import *
from planet_class import Planet

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt

import numpy as np




sun = Planet(name = "Sun", 
             mass = 1.989 * 10 ** 30, 
             semi_major_axis = 0,
             orbital_eccentricity =  0,
             orbital_inclination = 0,
             initial_polar_angle= 0,
             radius = 10,
             rotational_period = 0,
             orbital_period = 0.0001,
             color = (255, 255, 0),
             y_vel = 0)

sun.sun = True


mercury = Planet(name = "Mercury",
                 mass = 0.330 * 10 ** 24,
                 semi_major_axis = 0.39,
                 orbital_eccentricity = 0.206,
                 orbital_inclination = 7, 
                 initial_polar_angle = 2 * np.pi * np.random.rand(),
                 radius = 10,
                 rotational_period = 58.65,
                 orbital_period = 0.241,
                 color = (128, 128, 128),
                 y_vel = 47.4 * 1000)


venus = Planet(name = "Venus",
               mass = 4.87 * 10 ** 24,
               semi_major_axis = 0.72,
               orbital_eccentricity = 0.007,
               orbital_inclination = 3.4,
               initial_polar_angle = 2 * np.pi * np.random.rand(),
               radius = 10,
               rotational_period = 243.021,
               orbital_period = 0.616,
               color = (212, 204, 44),
               y_vel = 35 * 1000)


earth = Planet(name = "Earth",
               mass =  5.97 * 10 ** 24,
               semi_major_axis = 1,
               orbital_eccentricity = 0.017, 
               orbital_inclination = 0,
               initial_polar_angle = 2 * np.pi * np.random.rand(),
               radius = 10, 
               rotational_period = 1,
               orbital_period = 1,
               color = (0, 0, 255),
               y_vel = 29.8 * 1000)


mars = Planet(name = "Mars",
              mass = 0.642 * 10 ** 24, 
              semi_major_axis = 1.523,
              orbital_eccentricity = 0.094,
              orbital_inclination = 1.85, 
              initial_polar_angle = 2 * np.pi * np.random.rand(),
              radius = 10,
              rotational_period = 1.025,
              orbital_period = 1.882, 
              color = (255, 0, 0),
              y_vel = 24.1 * 1000)


jupiter = Planet(name = "Jupiter",
                 mass =  1898 * 10 ** 24,
                 semi_major_axis = 5.203, 
                 orbital_eccentricity = 0.049,
                 orbital_inclination = 1.31,
                 initial_polar_angle = 2 * np.pi * np.random.rand(),
                 radius = 10,
                 rotational_period = 0.4125, 
                 orbital_period = 11.866, 
                 color = (188, 68, 68),
                 y_vel = 13.1 * 1000)


saturn = Planet(name = "Saturn",
                mass = 568 * 10 ** 24, 
                semi_major_axis = 9.582, 
                orbital_eccentricity = 0.052, 
                orbital_inclination = 2.49, 
                initial_polar_angle = 2 * np.pi * np.random.rand(), 
                radius = 10, 
                rotational_period = 0.446,
                orbital_period = 29.444,
                color = (244, 194, 12),
                y_vel = 9.7 * 1000) 


uranus = Planet(name = "Uranus",
                mass = 86.8 * 10  ** 24, 
                semi_major_axis = 19.22, 
                orbital_eccentricity = 0.047, 
                orbital_inclination = 0.77, 
                initial_polar_angle = 2 * np.pi * np.random.rand(),
                radius = 10,
                rotational_period = 0.717, 
                orbital_period = 83.805, 
                color = (14, 242, 231),
                y_vel = 6.8 * 1000)


neptune = Planet(name = "Neptune",
                 mass = 102 * 10 ** 24,
                 semi_major_axis = 30.05,
                 orbital_eccentricity = 0.01, 
                 orbital_inclination = 1.77,
                 initial_polar_angle = 2 * np.pi * np.random.rand(),
                 radius = 10, 
                 rotational_period = 0.671,
                 orbital_period = 163.836, 
                 color = (1, 98, 255),
                 y_vel = 5.4 * 1000)


pluto = Planet(name = "Pluto",
               mass = 0.0130,
               semi_major_axis = 39.48,
               orbital_eccentricity = 0.244, 
               orbital_inclination = 17.2,
               initial_polar_angle = 2 * np.pi * np.random.rand(),
               radius = 10, 
               rotational_period = 6.388, 
               orbital_period = 248.110, 
               color = (149, 107, 107),
               y_vel = 4.7 * 1000)

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
inner_planets = [mercury, venus, earth, mars]
outer_planets = [jupiter, saturn, uranus, neptune, pluto]

# Create a Tkinter window
root = tk.Tk()
root.title("Solar System App")

# Configure the default font
root.option_add("*Font", "Roboto 12")

# Function to show matplotlib graphs in a Tkinter frame
def show_matplotlib_graph(fig, screen):
    canvas = FigureCanvasTkAgg(fig, master=screen)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Function to handle button presses and open task screens
def open_task_screen(task_name, task_function):
    new_screen = tk.Toplevel(root)
    new_screen.title(task_name)
    
    back_button = tk.Button(new_screen, text="Back to Menu", command=new_screen.destroy)
    back_button.pack()
    
    task_function(new_screen)  # Call the respective task function passing the new screen

# Task 1 function
def task1_screen(screen):
    fig = task1(planets)
    show_matplotlib_graph(fig, screen)

# Task 2 function
def task2_screen(screen):
    def update_graph():
        if graph_frame.winfo_children():
            graph_frame.winfo_children()[0].destroy()  # Destroy the previous graph

        selected_planets = inner_planets if planets_var.get() == "Inner Planets" else outer_planets
        selected_dimensions = dimensions_var.get()
        fig = task2(selected_planets, dimensions=selected_dimensions)
        show_matplotlib_graph(fig, graph_frame)

    dimensions_var = tk.StringVar()
    dimensions_var.set("2D")
    
    dimensions_frame = tk.Frame(screen)
    dimensions_frame.pack()
    
    dimensions_label = tk.Label(dimensions_frame, text="Select Dimensions:")
    dimensions_label.pack(side="left", padx=10)
    
    dimensions_2d_radio = tk.Radiobutton(dimensions_frame, text="2D", variable=dimensions_var, value="2D")
    dimensions_2d_radio.pack(side="left")
    
    dimensions_3d_radio = tk.Radiobutton(dimensions_frame, text="3D", variable=dimensions_var, value="3D")
    dimensions_3d_radio.pack(side="left")
    
    planets_var = tk.StringVar()
    planets_var.set("Inner Planets")
    
    planets_frame = tk.Frame(screen)
    planets_frame.pack()
    
    inner_button = tk.Radiobutton(planets_frame, text="Inner Planets", variable=planets_var, value="Inner Planets", command=update_graph)
    inner_button.pack(side="left", padx=10)
    
    outer_button = tk.Radiobutton(planets_frame, text="Outer Planets", variable=planets_var, value="Outer Planets", command=update_graph)
    outer_button.pack(side="left", padx=10)
    
    graph_frame = tk.Frame(screen)
    graph_frame.pack()

    # Initial graph display
    update_graph()

# Task 3 function
def task3_screen(screen):
    def update_animation():
        if graph_frame.winfo_children():
            graph_frame.winfo_children()[0].destroy()  # Destroy the previous animation

        selected_planets = inner_planets if planets_var.get() == "Inner Planets" else outer_planets
        animation = task3(selected_planets, limits=2.5 if planets_var.get() == "Inner Planets" else 50)
        animation_canvas = FigureCanvasTkAgg(animation, master=graph_frame)
        animation_canvas.get_tk_widget().pack()
        animation_canvas.draw()

    planets_var = tk.StringVar()
    planets_var.set("Inner Planets")
    
    planets_frame = tk.Frame(screen)
    planets_frame.pack()
    
    inner_button = tk.Radiobutton(planets_frame, text="Inner Planets", variable=planets_var, value="Inner Planets", command=update_animation)
    inner_button.pack(side="left", padx=10)
    
    outer_button = tk.Radiobutton(planets_frame, text="Outer Planets", variable=planets_var, value="Outer Planets", command=update_animation)
    outer_button.pack(side="left", padx=10)
    
    graph_frame = tk.Frame(screen)
    graph_frame.pack()

    # Initial animation display
    update_animation()

# Task 4 function
def task4_screen(screen):
    def update_animation():
        if graph_frame.winfo_children():
            graph_frame.winfo_children()[0].destroy()  # Destroy the previous animation

        selected_planets = inner_planets if planets_var.get() == "Inner Planets" else outer_planets
        animation = task4(selected_planets)
        animation_canvas = FigureCanvasTkAgg(animation, master=graph_frame)
        animation_canvas.get_tk_widget().pack()
        animation_canvas.draw()

    planets_var = tk.StringVar()
    planets_var.set("Inner Planets")
    
    planets_frame = tk.Frame(screen)
    planets_frame.pack()
    
    inner_button = tk.Radiobutton(planets_frame, text="Inner Planets", variable=planets_var, value="Inner Planets", command=update_animation)
    inner_button.pack(side="left", padx=10)
    
    outer_button = tk.Radiobutton(planets_frame, text="Outer Planets", variable=planets_var, value="Outer Planets", command=update_animation)
    outer_button.pack(side="left", padx=10)
    
    graph_frame = tk.Frame(screen)
    graph_frame.pack()

    # Initial animation display
    update_animation()


# Task 5 function
def task5_screen(screen):
    fig = task5(planets[-1])
    show_matplotlib_graph(fig, screen)

# Task 6 function
def task6_screen(screen):
    def update_animation():
        if graph_frame.winfo_children():
            graph_frame.winfo_children()[0].destroy()  # Destroy the previous animation

        options = options_var.get()
        planets_combinations = {
            1: {"planets": [sun, venus, earth], "scale": 250 / Planet.AU, "timestep": 3600 * 125},
            2: {"planets": [sun, jupiter, saturn], "scale": 40 / Planet.AU, "timestep": 3600 * 1500},
            3: {"planets": [sun, mercury, earth], "scale": 350 / Planet.AU, "timestep": 3600 * 75},
            4: {"planets": [sun, uranus, neptune], "scale": 15 / Planet.AU, "timestep": 3600 * 8000},
            5: {"planets": [sun, neptune, pluto], "scale": 10 / Planet.AU, "timestep": 3600 * 10000},
            6: {"planets": [sun, venus, mars], "scale": 250 / Planet.AU, "timestep": 3600 * 125}
        }
        selected_combination = planets_combinations.get(options, planets_combinations[1])  # Default to Venus-Earth

        animation = task6(selected_combination["planets"], SCALE=selected_combination["scale"], TIMESTEP=selected_combination["timestep"])
        animation_canvas = FigureCanvasTkAgg(animation, master=graph_frame)
        animation_canvas.get_tk_widget().pack()
        animation_canvas.draw()

    options_var = tk.IntVar()
    
    options_frame = tk.Frame(screen)
    options_frame.pack()

    options_label = tk.Label(options_frame, text="Select Spirograph Option:")
    options_label.pack(side="left", padx=10)

    for option_num, option_name in enumerate(["Venus-Earth", "Jupiter-Saturn", "Mercury-Earth", "Uranus-Neptune", "Neptune-Pluto", "Venus-Mars"]):
        option_button = tk.Radiobutton(options_frame, text=option_name, variable=options_var, value=option_num + 1, command=update_animation)
        option_button.pack(side="left", padx=10)
    
    graph_frame = tk.Frame(screen)
    graph_frame.pack()

    # Initial animation display
    update_animation()


# Task 7 function
def task7_screen(screen):
    task7()

# Quit function
def quit_app():
    root.destroy()

# Create buttons for each task
tasks = [
    ("Task 1", lambda: open_task_screen("Task 1", task1_screen)),
    ("Task 2", lambda: open_task_screen("Task 2", task2_screen)),
    ("Task 3", lambda: open_task_screen("Task 3", task3_screen)),
    ("Task 4", lambda: open_task_screen("Task 4", task4_screen)),
    ("Task 5", lambda: open_task_screen("Task 5", task5_screen)),
    ("Task 6", lambda: open_task_screen("Task 6", task6_screen)),
    ("Task 7", lambda: open_task_screen("Task 7", task7_screen)),
    ("Quit", quit_app)
]

for task_name, task_function in tasks:
    button = tk.Button(root, text=task_name, command=task_function, height=2, width=15)
    button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()