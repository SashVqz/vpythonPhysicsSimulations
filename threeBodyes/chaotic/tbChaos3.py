from vpython import *
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1  
planets = []
massCentral = 3
massSide = 1.5
distance = 1.5

kineticEnergy1 = []
kineticEnergy2 = []
kineticEnergy3 = []
totalEnergy = []

p = sphere(pos=vector(0, 0, 0), radius=0.05, color=color.red, mass=massCentral, make_trail=True, trail_type='points', interval=25, retain=15)
planets.append(p)
p = sphere(pos=vector(-1, 0, 0), radius=0.05, color=color.blue, mass=massSide, make_trail=True, trail_type='points', interval=25, retain=15)
planets.append(p)
p = sphere(pos=vector(1, 0, 0), radius=0.05, color=color.cyan, mass=massSide, make_trail=True, trail_type='points', interval=25, retain=15)
planets.append(p)

vSide = np.sqrt(G * massCentral / distance)

planets[0].velocity = vector(0, 0, 0)
planets[1].velocity = vector(0, vSide, 0)
planets[2].velocity = vector(0, -vSide, 0)

dt = 0.01

def calculateForces(planet1, planet2):
    r = planet2.pos - planet1.pos
    rMag = mag(r)
    F = G * planet1.mass * planet2.mass / rMag**2
    F = norm(r) * F
    return F

numIterations = 1000
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
plt.plot(kineticEnergy1, label='Central Planet', color='red', linestyle='--')
plt.plot(kineticEnergy2, label='Left Planet', color='blue', linestyle='-.')
plt.plot(kineticEnergy3, label='Right Planet', color='cyan', linestyle=':')
plt.plot(totalEnergy, label='Total', color='green', linewidth=2)
plt.xlabel('Iteration')
plt.ylabel('Kinetic Energy')
plt.title('Kinetic Energy Variation of Planets Over Time')
plt.legend()
plt.grid(True)
plt.show()
