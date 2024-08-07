from vpython import *
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1  
planets = []
mass = 2

kineticEnergy1 = []
kineticEnergy2 = []
kineticEnergy3 = []
totalEnergy = []

p = sphere(pos=vector(-2, 0, 0), radius=0.09, color=color.red, mass=0.3, make_trail=True, trail_type='points', interval=25, retain=15)
planets.append(p)
p = sphere(pos=vector(0, 0, 0), radius=0.09, color=color.blue, mass=mass, make_trail=True, trail_type='points', interval=25, retain=15)
planets.append(p)
p = sphere(pos=vector(3, 1, 0), radius=0.09, color=color.cyan, mass=0.3, make_trail=True, trail_type='points', interval=25, retain=15)
planets.append(p)

distance = mag(planets[0].pos - planets[1].pos)
v = np.sqrt(G * mass / distance)
vc = np.sqrt(G * 0.3 / distance)

planets[0].velocity = vector(0, v, 0)
planets[1].velocity = vector(vc / 10, vc, 0)
planets[2].velocity = vector(-v / 2, v / 2, 0)

dt = 0.02

def calculateForces(planet1, planet2):
    r = planet2.pos - planet1.pos
    rMag = mag(r)
    F = G * planet1.mass * planet2.mass / rMag**2
    F = norm(r) * F
    return F

numIterations = 250
currentIteration = 0

# Simulation loop
while currentIteration < numIterations:
    rate(20)
    for n in range(3):
        planets[n].pos += planets[n].velocity * dt

        netForce = vector(0, 0, 0)
        for m in range(3):
            if n != m:
                if m > n:
                    netForce += calculateForces(planets[n], planets[m])
                else:
                    netForce -= calculateForces(planets[m], planets[n])

        planets[n].velocity += (netForce * dt / planets[n].mass)

        kineticEnergy = 0.5 * planets[n].mass * mag(planets[n].velocity)**2
        if n == 0:
            kineticEnergy1.append(kineticEnergy)
        elif n == 1:
            kineticEnergy2.append(kineticEnergy)
        else:
            kineticEnergy3.append(kineticEnergy)

    totalEnergy.append(sum([kineticEnergy1[-1], kineticEnergy2[-1], kineticEnergy3[-1]]))
    currentIteration += 1

# plot
plt.figure(figsize=(12, 6))
plt.plot(kineticEnergy1, label='Planet 1', color='red', linestyle='--')
plt.plot(kineticEnergy2, label='Planet 2', color='blue', linestyle='-.')
plt.plot(kineticEnergy3, label='Planet 3', color='cyan', linestyle=':')
plt.plot(totalEnergy, label='Total', color='green', linewidth=2)
plt.xlabel('Iteration')
plt.ylabel('Kinetic Energy')
plt.title('Kinetic Energy Variation of Planets Over Time')
plt.legend()
plt.grid(True)
plt.show()
