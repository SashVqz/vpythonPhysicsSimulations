from vpython import *
import numpy as np
from math import sqrt

# Constants
G = 6.67430e-11
M_Pluto = 1.303e22
M_Charon = 1.586e21
R = 1.957e7 # Distance between Pluto and Charon (m)
e = 0.1
a = R / (1 - e) 

v = sqrt(G * (M_Pluto + M_Charon) * (2 / R - 1 / a))

initial_pos_Pluto = vector(-R * M_Charon / (M_Pluto + M_Charon), 0, 0)
initial_pos_Charon = vector(R * M_Pluto / (M_Pluto + M_Charon), 0, 0)

v_Pluto = v * M_Charon / (M_Pluto + M_Charon)
v_Charon = v * M_Pluto / (M_Pluto + M_Charon)

Pluto = sphere(pos=initial_pos_Pluto, radius=1e6, color=color.blue, mass=M_Pluto, make_trail=True)
Charon = sphere(pos=initial_pos_Charon, radius=1e6, color=color.white, mass=M_Charon, make_trail=True)

Pluto.velocity = vector(0, -v_Pluto, 0)
Charon.velocity = vector(0, v_Charon, 0)

dt = 500  # seconds

# plot
scene = graph(title='Kinetic Energy of Pluto and Charon', xtitle='Time (s)', ytitle='Kinetic Energy (J)')
kinetic_curve_pluto = gcurve(graph=scene, color=color.blue, label='Pluto')
kinetic_curve_charon = gcurve(graph=scene, color=color.red, label='Charon')

# Simulation loop
t = 0
while True:
    rate(100)

    r = Charon.pos - Pluto.pos
    r_mag = mag(r)
    F = G * Pluto.mass * Charon.mass / r_mag**2
    F_vec = norm(r) * F

    Pluto.velocity += F_vec * dt / Pluto.mass
    Charon.velocity -= F_vec * dt / Charon.mass

    Pluto.pos += Pluto.velocity * dt
    Charon.pos += Charon.velocity * dt

    kinetic_energy_pluto = 0.5 * Pluto.mass * mag(Pluto.velocity)**2
    kinetic_energy_charon = 0.5 * Charon.mass * mag(Charon.velocity)**2
    kinetic_curve_pluto.plot(t, kinetic_energy_pluto)
    kinetic_curve_charon.plot(t, kinetic_energy_charon)

    t += dt
